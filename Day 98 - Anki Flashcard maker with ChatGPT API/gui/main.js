const { app, BrowserWindow } = require('electron')
const {PythonShell} = require('python-shell')
const path = require('path')


const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,  // for Node in renderer
            contextIsolation: false
        }
    })  
    win.loadFile('templates/index.html')
}

app.whenReady().then(() => {
    createWindow()

    var options = {
        scriptPath : path.join(__dirname),
        args : [],
    };

    let pyshell = new PythonShell('test2.py', options);

    pyshell.on('message', function(message) {
        console.log(message);
        console.log(typeof message);
    });
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit()
})

// npm run start
