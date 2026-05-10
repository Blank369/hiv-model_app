export function getGammaLabel(mode) {
    switch (mode) {
        case 'THERAPY': return 'День начала терапии'
        case 'INTERRUPTION': return 'Период между приемами (сут)'
        case 'RESISTANCE': return 'Скорость резистентности'
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