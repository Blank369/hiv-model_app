export function createAbortController() {
    const controller = new AbortController()
    return { controller, signal: controller.signal }
}

export function handleApiError(error, defaultMessage) {
    if (error.name === 'AbortError' || error.code === 'ERR_CANCELED') {
        return { success: false, error: 'Операция прервана', aborted: true }
    }
    console.error(error)
    return { success: false, error: defaultMessage }
}

export function downloadBlob(blob, filename) {
    const url = window.URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.setAttribute('download', filename)
    document.body.appendChild(link)
    link.click()
    link.remove()
    window.URL.revokeObjectURL(url)
}

export function getTimestampedFilename(baseName) {
    const now = new Date()
    const timestamp = now.toISOString().slice(0, 19).replace(/:/g, '-')
    return `${baseName}_${timestamp}.txt`
}