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

contextBridge.exposeInMainWorld('lockInput', {
  lockInput: (callback) => ipcRenderer.on('freeze-content', (_event, value) => callback(value))
})