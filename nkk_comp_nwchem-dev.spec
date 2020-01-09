/*
A KBase module: nkk_comp_nwchem-dev
*/

module nkk_comp_nwchem-dev {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_nkk_comp_nwchem-dev(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
