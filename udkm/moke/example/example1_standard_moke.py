import udkm.moke.functions as moke

parameter_file_name = "parameters/parameters_example_1.txt"

line = 0

params = moke.get_scan_parameter(parameter_file_name, line)
params["bool_t0_shift"] = True
params["bool_save_plot"] = True
params["t0_column_name"] = "moke"
params["plot_path"] = "plot_overview//"
params["t_max"] = 1000
params["scan_path"] = "scan_export//"


scan = moke.load_overview_data(params)

moke.plot_overview(scan,**params)

# Save scan dictionary into a pickle file.
moke.save_scan(scan)
# Load a scan from a pickle file
scan1 = moke.load_scan("20211119", "092027", "scan_export/")
moke.plot_overview(scan1, t_max = 2000)
