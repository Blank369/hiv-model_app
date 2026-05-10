import apiClient from '@/api'
import { createAbortController, handleApiError, downloadBlob, getTimestampedFilename} from "@/utils/apiHelpers.js";

export const simulationService = {
    abortController: null,

    async simulate(params) {
        if (this.abortController) {
            this.abortController.abort()
        }

        const { controller, signal } = createAbortController()
        this.abortController = controller

        try {
            const response = await apiClient.post('/simulate', params, { signal })
            return { success: true, data: response.data }
        } catch (error) {
            return handleApiError(error, 'Не удалось выполнить расчёт')
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
            return handleApiError(error, 'Сервер недоступен')
        }
    },

    async downloadResult() {
        try {
            const response = await apiClient.get('/download-results', {
                responseType: 'blob'
            })

            const filename = getTimestampedFilename('results')
            downloadBlob(response.data, filename)

            return { success: true }
        } catch (error) {
            return handleApiError(error, 'Не удалось скачать файл')
        }
    }
}