export function getGammaLabel(mode) {
    switch (mode) {
        case 'THERAPY': return 'Day of therapy initiation'
        case 'INTERRUPTION': return 'Interval between doses (days)'
        case 'RESISTANCE': return 'Resistance development rate'
        default: return 'γ'
    }
}

export function getGammaStep(mode) {
    switch (mode) {
        case 'THERAPY': return 1
        case 'INTERRUPTION': return 0.1
        case 'RESISTANCE': return 0.001
        default: return 0.001
    }
}