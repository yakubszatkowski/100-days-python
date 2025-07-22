const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('openFileApi', {
    openFile: () => {return ipcRenderer.invoke('open-file')}
})

contextBridge.exposeInMainWorld('sendData', {
    toMain: (data) => {ipcRenderer.send('data-receive', data)}
})

// TODO: ERROR DIALOG