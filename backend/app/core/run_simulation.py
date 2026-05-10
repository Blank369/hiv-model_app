from .init_simulation_helpers import (
    parse_request,
    create_initial_conditions,
    create_bio_params,
    create_diff_eq_classes,
    create_epsilon,
    create_time_params,
    create_params_dict,
    format_response
)
from .solve_model import solve_model
from ..utils import write_table

def run_simulation(request_data: dict) -> dict:
    initials, bio, virus, immune, therapy, sim = parse_request(request_data)

    initial_conditions = create_initial_conditions(initials)
    bio_params = create_bio_params(bio, virus, immune)
    equations = create_diff_eq_classes(bio_params)
    epsilon = create_epsilon(therapy)
    time_params = create_time_params(sim)

    params_dict = create_params_dict(initials, bio, virus, immune, therapy, sim)

    simulation = solve_model(initial_conditions, time_params, equations, epsilon)

    write_table("result", simulation, params_dict)

    return format_response(simulation)