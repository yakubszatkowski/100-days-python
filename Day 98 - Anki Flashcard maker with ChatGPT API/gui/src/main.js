const { app, BrowserWindow } = require('electron/main')
const path = require('path')
const {PythonShell} = require('python-shell')

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            contextIsolation: false,
            nodeIntegration: true,
            preload: path.join(__dirname, 'preload.js')
        },
    })
    win.loadFile('templates/index.html')
    win.webContents.openDevTools()
}

app.whenReady().then(() => {
    createWindow()

    var options = {
        scriptPath : path.join(__dirname),
        args : [],
    };
    
    let pyshell = new PythonShell('../../engine/main.py', options);
    
    pyshell.on('message', function(message) {
        console.log(message);
     console.log(typeof message);
    });

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow()
        }
    })
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})
