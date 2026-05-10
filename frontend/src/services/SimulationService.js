import apiClient from '@/api'

export const simulationService = {
    // Хранилище для контроллера отмены
    abortController: null,

    async simulate(params) {
        if (this.abortController) {
            this.abortController.abort()
        }

        this.abortController = new AbortController()

        try {
            const response = await apiClient.post('/simulate', params, {
                signal: this.abortController.signal
            })
            return { success: true, data: response.data }
        } catch (error) {
            if (error.name === 'AbortError' || error.code === 'ERR_CANCELED') {
                return { success: false, error: 'Расчет прерван', aborted: true }
            }
            return {
                success: false,
            }
        } finally {
            this.abortController = null
        }
    },

    abort() {
        if (this.abortController) {
            this.abortController.abort()
            this.abortController = null
        }
    },

    async check() {
        try {
            const response = await apiClient.get('/check')
            return { success: true, data: response.data }
        } catch (error) {
            console.error('Ошибка при вызове /health:', error)
            return { success: false, error: 'Сервер недоступен' }
        }
    }
}