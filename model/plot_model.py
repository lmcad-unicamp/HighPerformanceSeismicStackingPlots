LOCALE_PT_BR = "pt_BR"
LOCALE_EN_US = "en_US"
LOCALE = LOCALE_EN_US


class GraphSize:
    MIDDLE = (9, 7)
    LARGE = (18, 6)


class Legends:
    INTERPOLATIONS_PER_SEC = {
        LOCALE_PT_BR: "Interpolações por segundo",
        LOCALE_EN_US: "Interpolations per second"
    }

    INTERPOLATIONS_PER_SEC_PER_GPU = {
        LOCALE_PT_BR: "Interpolações por segundo e por GPU",
        LOCALE_EN_US: "Interpolations per second per GPU"
    }

    AVG_INTERPOLATIONS_PER_SEC = {
        LOCALE_PT_BR: "Interpolações/s média",
        LOCALE_EN_US: "Average interpolations per second"
    }

    RELATIVE_PERFORMANCE = {
        LOCALE_PT_BR: "Desempenho relativo",
        LOCALE_EN_US: "Relative performance"
    }

    AVG_RELATIVE_PERFORMANCE = {
        LOCALE_PT_BR: "Desempenho relativo médio",
        LOCALE_EN_US: "Average relative performance"
    }

    EFFICIENCY = {
        LOCALE_PT_BR: "Eficiência",
        LOCALE_EN_US: "Efficiency"
    }

    EFFICIENCY_RATE = {
        LOCALE_PT_BR: '\%',
        LOCALE_EN_US: '\%'
    }

    TRACE_USE = {
        LOCALE_PT_BR: '\%',
        LOCALE_EN_US: '\%'
    }

    AVG_TRACE_USE = {
        LOCALE_PT_BR: '\% de uso de traços médio',
        LOCALE_EN_US: 'Average \% of used traces'
    }

    SECONDS = {
        LOCALE_PT_BR: 'Segundos',
        LOCALE_EN_US: 'Seconds'
    }

    THREAD_COUNT = {
        LOCALE_PT_BR: 'Número de threads',
        LOCALE_EN_US: 'Thread count'
    }

    HEURISTIC_ON = {
        LOCALE_PT_BR: 'Com heurística',
        LOCALE_EN_US: 'Heuristic ON'
    }

    HEURISTIC_OFF = {
        LOCALE_PT_BR: 'Sem heurística',
        LOCALE_EN_US: 'Heuristic OFF'
    }

    AVG_TOTAL_EXEC_TIME = {
        LOCALE_PT_BR: 'Tempo de execução médio',
        LOCALE_EN_US: 'Average execution time'
    }

    COST = {
        LOCALE_PT_BR: 'Custo médio',
        LOCALE_EN_US: 'Average cost'
    }

    DOLLARS = {
        LOCALE_PT_BR: 'Dólares americanos',
        LOCALE_EN_US: 'US Dollars'
    }

    NODE_COUNT = {
        LOCALE_PT_BR: 'Número de nós',
        LOCALE_EN_US: 'Node count'
    }

    DE = {
        LOCALE_PT_BR: 'Evolução diferencial',
        LOCALE_EN_US: 'Differential evolution'
    }

    GREEDY = {
        LOCALE_PT_BR: 'Busca linear',
        LOCALE_EN_US: 'Linear search'
    }
