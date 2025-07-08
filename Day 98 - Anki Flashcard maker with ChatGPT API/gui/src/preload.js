const {contextBridge, ipcRenderer} = require('electron')

contextBridge.exposeInMainWorld('openFileApi', {
    openFile: () => {return ipcRenderer.invoke('open-file')}
})