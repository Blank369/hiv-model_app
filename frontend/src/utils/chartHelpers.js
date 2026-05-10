const XAxis = {
    title: { display: true, text: 'Время (дни)' },
    ticks: {
        callback: (value) => {
            return Math.round(value)
        }
    },
    type: 'linear',
}

export const baseChartOptions = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
        legend: { position: 'top' },
        tooltip: { mode: 'index', intersect: false }
    },
    elements: {
        point: { radius: 0, hoverRadius: 4 },
        line: { tension: 0.3, borderWidth: 2 }
    }
}

export function createChartOptions(yAxisConfig) {
    return {
        ...baseChartOptions,
        scales: {
            x: XAxis,
            y: yAxisConfig
        }
    }
}

export const cellChartOptions = createChartOptions({
    title: { display: true, text: 'кл/мкл' }
})

export const virusChartOptions = createChartOptions({
    title: { display: true, text: 'копий/мл' },
})

export const therapyChartOptions = createChartOptions({
    title: { display: true, text: 'ε' },
    min: 0,
    max: 1
})

export const chartColors = {
    T: '#3b82f6',
    L: '#6366f1',
    I: '#8b5cf6',
    V: '#ec4899',
    C: '#14b8a6',

    eps_inf: '#355bae',
    eps_prod: '#4900cf'
}

export function createChartData(labels, data, label, color, options = {}) {
    return {
        labels: labels || [],
        datasets: [{
            label: label,
            data: data || [],
            borderColor: color,
            backgroundColor: 'transparent',
            tension: 0.3,
            fill: options.fill || false,
            ...options
        }]
    }
}