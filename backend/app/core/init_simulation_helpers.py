from ..model.Initials import Initials
from ..model.d_T import d_T
from ..model.d_L import d_L
from ..model.d_I import d_I
from ..model.d_V import d_V
from ..model.d_C import d_C
from ..model.Epsilon import Epsilon
from ..model.TimeParams import TimeParams

def parse_request(request_data: dict):
    return (
        request_data['initials'],
        request_data['biological'],
        request_data['virus'],
        request_data['immune'],
        request_data['therapy'],
        request_data['sim']
    )

def create_initial_conditions(initials: dict):
    return Initials(
        in_T=initials['T'],
        in_L=initials['L'],
        in_I=initials['I'],
        in_V=initials['V'],
        in_C=initials['C']
    )

def create_bio_params(bio: dict, virus: dict, immune: dict) -> dict:
    return {
        'lambda': bio['lambda'], 'r': bio['r'], 'T_max': bio['T_max'],
        'd_T': bio['d_T'], 'beta': bio['beta'], 'rho': bio['rho'],
        'a': bio['a'], 'delta_L': bio['delta_L'], 'delta_I': bio['delta_I'],
        'kappa': bio['kappa'],
        'p': virus['p'], 'c': virus['c'], 'phi': virus['phi'],
        's_C': immune['s_C'], 'alpha': immune['alpha'], 'h': immune['h'],
        'd_C': immune['d_C'], 'eta_C': immune['eta_C'], 'q': immune['q']
    }

def create_diff_eq_classes(bio_params: dict):
    dT = d_T(bio_params['lambda'], bio_params['r'], bio_params['T_max'], bio_params['d_T'], bio_params['beta'])
    dL = d_L(bio_params['rho'], bio_params['a'], bio_params['delta_L'], bio_params['beta'])
    dI = d_I(bio_params['delta_I'], bio_params['kappa'], bio_params['a'], bio_params['rho'], bio_params['beta'])
    dV = d_V(bio_params['p'], bio_params['c'], bio_params['phi'])
    dC = d_C(bio_params['s_C'], bio_params['alpha'], bio_params['h'], bio_params['d_C'], bio_params['eta_C'],
             bio_params['q'])
    return dT, dL, dI, dV, dC

def create_epsilon(therapy: dict):
    return Epsilon(
        epsilon0_inf=therapy['epsilon0_inf'],
        mode_inf=therapy['mode_inf'],
        gamma_inf=therapy['gamma_inf'],
        epsilon0_prod=therapy['epsilon0_prod'],
        mode_prod=therapy['mode_prod'],
        gamma_prod=therapy['gamma_prod']
    )

def create_time_params(sim: dict):
    t_max = sim['t_max']
    num_points = sim['num_points']
    tau = t_max / num_points
    return TimeParams(tau=tau, dpi_max=t_max)

def format_response(t, result):
    return {
        "t": t.tolist(),
        "T": result[:, 0].tolist(),
        "L": result[:, 1].tolist(),
        "I": result[:, 2].tolist(),
        "V": result[:, 3].tolist(),
        "C": result[:, 4].tolist()
    }