<<<<<<< Updated upstream
import unittest


class MyTestCase(unittest.TestCase):
    def test_presents_of_files(self):

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
=======
import unittest
import os
import sys
sys.path.insert(1, '../')
from build_data_file import*

##Global variables
region = "region"
startyear = 2012
endyear = 2040

class ImportTestCase(unittest.TestCase):
    def test_files_load_csvs_count_nr_loaded_csv_should_be_2(self):
        paths = (os.getcwd() + '\data')
        files = load_csvs(paths)
        assert len(files) == 19

    def test_noncsv_files_gives_error_message_and_exit(self):
        paths = (os.getcwd() + '\invalid_test_data')
        with self.assertRaises(SystemExit):
            load_csvs(paths)

    def test_import_OSeMOSYS_param_files_to_outPutFile_hej_hej(self):
        path = (os.getcwd())
        param_file = '\hej_hej.txt'
        text = make_outputfile(path, param_file)
        assert text == "hej\nhej"

    def test_TRLV_3_operational_life_should_be_60(self):
        paths = (os.getcwd() + '\data')
        dict_df = load_csvs(paths)
        param_file = '\osemosys_shell_param.txt'
        path = os.getcwd()
        outPutFile = make_outputfile(path, param_file)
        outPutFile = operational_life(outPutFile, dict_df['GIS_data'], region, dict_df['operational_life'])
        test = "region\tTRLV_3\t60\n"
        assert test in outPutFile

    def test_MG_5_fixed_cost_should_be_1_in_2027(self):
        paths = (os.getcwd() + '\data')
        dict_df = load_csvs(paths)
        param_file = '\osemosys_shell_param.txt'
        path = os.getcwd()
        outPutFile = make_outputfile(path, param_file)
        outPutFile = fixedcost(dict_df['GIS_data'], outPutFile, startyear, endyear, region, dict_df['fixed_cost'])
        print(outPutFile)
        test = "region\tMG_5\t2027\t1\n"
        assert test in outPutFile

    def test_SO_3_emissions_should_be_55_CO2_modeoperation_2_in_2027(self):
        paths = (os.getcwd() + '\data')
        dict_df = load_csvs(paths)
        param_file = '\osemosys_shell_param.txt'
        path = os.getcwd()
        modeofoperation = [1,2]
        outPutFile = make_outputfile(path, param_file)
        outPutFile = emissionactivity(dict_df['GIS_data'], outPutFile, startyear, endyear,region, dict_df['emissions'], modeofoperation)
        test = "region\tSO_3\tCO2\t2\t2027\t55\n"
        assert test in outPutFile

if __name__ == '__main__':
    unittest.main()
>>>>>>> Stashed changes
