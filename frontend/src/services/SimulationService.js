import apiClient from '@/api'

export const simulationService = {
    async simulate(params) {
        try {
            const response = await apiClient.post('/simulate', params)
            return { success: true, data: response.data }
        } catch (error) {
            console.error('Ошибка при вызове /simulate:', error)
            return {
                success: false,
                error: error.response?.data?.detail || 'Не удалось выполнить расчёт'
            }
        }
    },

    async check() {
        try {
            const response = await apiClient.get('/check')
            return { success: true, data: response.data }
        } catch (error) {
            console.error('Ошибка при вызове /check:', error)
            return { success: false, error: 'Сервер недоступен' }
        }
    }
}