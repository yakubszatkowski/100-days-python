import { app, BrowserWindow, ipcMain, dialog } from 'electron';
import path from 'node:path';
import started from 'electron-squirrel-startup';
import {PythonShell} from 'python-shell'
import dotenv from 'dotenv'

dotenv.config()

if (started) {
    app.quit();
}

const createWindow = () => {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
        },
    });
    // mainWindow.setAlwaysOnTop(true, 'screen');

    if (MAIN_WINDOW_VITE_DEV_SERVER_URL) {
        mainWindow.loadURL(MAIN_WINDOW_VITE_DEV_SERVER_URL);
    } else {
        mainWindow.loadFile(path.join(__dirname, `../renderer/${MAIN_WINDOW_VITE_NAME}/index.html`));
    }

    mainWindow.webContents.openDevTools();
};

const pyOptions = {
    scriptPath : path.join(__dirname, '../../../engine/'),
    pythonPath: process.env.PYTHON_PATH,
    pythonOptions: ['-u'],
    encoding: 'utf8',
    args : [],
};
const pyShellMain = new PythonShell('a_main.py', pyOptions);

const dialogOptions = {
    filters: [{ name: 'PDF', extensions: ['pdf'] } ]
}

app.whenReady().then(() => {
    createWindow();
    
    ipcMain.handle('open-file', async () => {
        const {canceled, filePaths} = await dialog.showOpenDialog(dialogOptions)
        if (!canceled) {
            return filePaths[0]
        }
    })

    ipcMain.on('data-receive', (e, data) => {
        pyShellMain.send(JSON.stringify(data), { mode: 'json' });
    })

    ipcMain.on('open-error', () => {
        dialog.showErrorBox('Error', 'You must only enter .pdf files.')
    })

    pyShellMain.on('message', function(message) {
        if (message == 'False') {
            dialog.showErrorBox('Error', 'This file doesn\'t exist!')
        } else {
            console.log(message);
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
