import pandapower as pp
import pandapower.networks as pn
from pandapower.plotting.plotly import pf_res_plotly 

def load_all_phases(net):
    '''adds a load to every phase that is currently at 0'''
    load_data_frame = net.asymmetric_load
    new_value = 0.000114 
    load_data_frame.replace(to_replace=0, value=new_value, inplace=True) # replace all 0s with new value
    net.asymmetric_load = load_data_frame
    return net

def main():
    net = pn.ieee_european_lv_asymmetric('on_peak_566') # create network
    net = load_all_phases(net) # add load wherever the load is 0

    print("Asymmetric load table:")
    print(net.asymmetric_load) 

    pp.runpp_3ph(net) # run the three-phase powerflow
    # pp.runpp(net) # run standard powerflow

    print("Result asymmetric load table:")
    print(net.res_asymmetric_load)

main()
