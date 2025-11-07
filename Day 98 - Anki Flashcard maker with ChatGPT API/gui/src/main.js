import { app, BrowserWindow, ipcMain, dialog } from 'electron';
import path from 'node:path';
import started from 'electron-squirrel-startup';
import {PythonShell} from 'python-shell'
import dotenv from 'dotenv'
import { createSplash, changeSplash } from './splash.js';

dotenv.config()

if (started) {
    app.quit();
}

const createWindow = () => {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 500,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
        },
        alwaysOnTop: true
    });

    if (MAIN_WINDOW_VITE_DEV_SERVER_URL) {
        mainWindow.loadURL(MAIN_WINDOW_VITE_DEV_SERVER_URL);
    } else {
        mainWindow.loadFile(path.join(__dirname, `../renderer/${MAIN_WINDOW_VITE_NAME}/index.html`));
    }

    // mainWindow.webContents.openDevTools();

    return mainWindow
};

const pyOptions = {
    scriptPath : path.join(__dirname, '../../../engine/'),
    pythonPath: process.env.PYTHON_PATH,
    pythonOptions: ['-u'],
    encoding: 'utf8',
    args : [],
};
const pyShellMain = new PythonShell('a_main.py', pyOptions);

const openDialogOptions = {
    filters: [{ name: 'PDF', extensions: ['pdf'] } ]
}

const saveDialogOptions = {
    filters: [{ name: 'CSV', extensions: ['csv'] } ],
    defaultPath: path.join(app.getPath('downloads'), 'myflashcards')
}

let dialogOpened = false;

app.whenReady().then(() => {
    const mainWindow = createWindow();
    var loadingSplash

    ipcMain.handle('open-file', async () => {
        if (dialogOpened) return null
        dialogOpened = true
        const {canceled, filePaths} = await dialog.showOpenDialog(openDialogOptions)
        if (!canceled) {
            dialogOpened = false
            return filePaths[0]
        } else {
            dialogOpened = false
        }
    });

    ipcMain.handle('save-directory', async () => {
        if (dialogOpened) return null
        dialogOpened = true
        const { canceled, filePath } = await dialog.showSaveDialog(saveDialogOptions);
        if (!canceled) {
            dialogOpened = false
            return filePath;
        } else {
            dialogOpened = false
        }
    });

    ipcMain.on('data-receive', (e, data) => {
        pyShellMain.send(JSON.stringify(data), { mode: 'json' });
    });

    ipcMain.on('open-error', () => {
        dialog.showErrorBox('Error', 'You must only enter .pdf files.')
    });

    pyShellMain.on('message', (message) => {
        console.log(message)
        if (message == 'False') {
            dialog.showErrorBox('Error', 'This file doesn\'t exist!')
        } else {
            if (message == 'Input successful') {
                mainWindow.webContents.send('freeze-content', 1);
                loadingSplash = createSplash();

            };
            if (message == 'Done') {
                mainWindow.webContents.send('freeze-content', 0);
            };
        };

        if (loadingSplash) {
            loadingSplash.webContents.send('progress-text-change', message)
            if (message == 'Done') {
                loadingSplash.destroy()
            }
        }

    });

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});


app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
