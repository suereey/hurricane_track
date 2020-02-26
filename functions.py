import os
import numpy
import progressbar


def function_assemble_raw_data():
    array_latitude_bin_edge = numpy.arange(-91, 91,2)
    array_latitude_bin_center = numpy.arange(-90, 90,2)
    array_longitude_bin_edge = numpy.arange(0, 361,2) - 1
    array_longitude_bin_center = numpy.arange(1, 360,2) - 1
    for i_longitude in range(len(array_longitude_bin_center)):
        if array_longitude_bin_center[i_longitude] > 180:
            array_longitude_bin_center[i_longitude] \
                = array_longitude_bin_center[i_longitude] \
                - 360
    for i_longitude in range(len(array_longitude_bin_edge)):
        if array_longitude_bin_edge[i_longitude] > 180:
            array_longitude_bin_edge[i_longitude] \
                = array_longitude_bin_edge[i_longitude] \
                - 360

    array_latitude_bin_center_index = numpy.arange(0, 90, 1)
    array_longitude_bin_center_index = numpy.arange(0, 180, 1)
    array_latitude_bin_edge_index = numpy.arange(0, 91, 1)
    array_longitude_bin_edge_index = numpy.arange(0, 181, 1)
    dict_sea_surface_temperature_data = {}
    bar =  progressbar.ProgressBar(
        min_value = 1880, 
        max_value= 2020, 
        initial_value=1880)
    bar.start()
    for i_year in range(1880, 2020):
        bar.update(i_year)
        # print('processing year: {}'.format(i_year))
        list_year_data = []
        rawdata \
            = numpy.loadtxt(
                'data/raw_data/ersst_v5_ascii/ersst.v5.{:4.0f}.asc'.format(i_year))
        for int_month in range(1, 13):
            array2d_monthly_data \
                = rawdata[(int_month - 1) * 180: int_month * 180,:] / 100
            array2d_monthly_data \
                = numpy.append(
                    array2d_monthly_data[:,:1], 
                    array2d_monthly_data, 
                    axis = 1)
            array2d_monthly_data \
                = numpy.append(
                    array2d_monthly_data, 
                    array2d_monthly_data[:,-1:], 
                    axis = 1)
            list_year_data.append(array2d_monthly_data)
        dict_sea_surface_temperature_data['{}'.format(i_year)] = list_year_data
    
    bar.finish()
    numpy.savez(
        'data/ersst_v5', 
        dict_sea_surface_temperature_data = dict_sea_surface_temperature_data, 
        array_longitude_bin_edge_index = array_longitude_bin_edge_index, 
        array_longitude_bin_edge = array_longitude_bin_edge, 
        array_latitude_bin_edge_index = array_latitude_bin_edge_index, 
        array_latitude_bin_edge = array_latitude_bin_edge, 
        array_longitude_bin_center_index = array_longitude_bin_center_index, 
        array_longitude_bin_center = array_longitude_bin_center, 
        array_latitude_bin_center_index = array_latitude_bin_center_index, 
        array_latitude_bin_center = array_latitude_bin_center)
    print("Wrote formatted data to file:", 'data/ersst_v5')
    return None