import {BrowserWindow} from 'electron';
import path from 'node:path';


export const createSplash = () => {
    const splash = new BrowserWindow({
        width: 400, 
        height: 200, 
        transparent: true, 
        frame: false, 
        alwaysOnTop: true,
        webPreferences: {
            preload: path.join(__dirname, '../../src/splash-preload.js'),
        },
    });
    const splashDir = path.join(__dirname, '../../src/splash.html')
    splash.loadFile(splashDir)

    // splash.webContents.openDevTools();

    return splash
}

export const changeSplash = () => {
    console.log(helloworld)
}