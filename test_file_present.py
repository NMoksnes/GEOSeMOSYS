import unittest
from build_data_file import*

#Testcases:
# see that imported files are only csv
#
class ImportTestCase(unittest.TestCase):
    def test_empty_files_return_outputfile(self):
        outPutFile = [1]
        inputactivity = []
        startyear = 2012
        endyear = 2040
        region = "region"
        modeofoperation = [1]
        inputact(outPutFile, inputactivity, startyear, endyear, region, modeofoperation)
        assert outPutFile is not None

    def test_imported_files_are_csv(self):
        paths = r'C:\Windows'
        load_csvs(paths)
        assertRaises()

if __name__ == '__main__':
    unittest.main()
