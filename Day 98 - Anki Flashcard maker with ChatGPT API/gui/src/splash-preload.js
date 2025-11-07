const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('changeText', {
  changeText: (callback) => ipcRenderer.on('progress-text-change', (_event, value) => callback(value))
})