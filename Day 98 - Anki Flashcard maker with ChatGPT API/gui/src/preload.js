const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('openFileApi', {
    openFile: () => {return ipcRenderer.invoke('open-file')}
})

contextBridge.exposeInMainWorld('saveDirectoryApi', {
    saveDirectory: () => {return ipcRenderer.invoke('save-directory')}
})

contextBridge.exposeInMainWorld('sendData', {
    toMain: (data) => {ipcRenderer.send('data-receive', data)}
})

contextBridge.exposeInMainWorld('showError', {
    toMainError: () => {ipcRenderer.send('open-error')}
})
