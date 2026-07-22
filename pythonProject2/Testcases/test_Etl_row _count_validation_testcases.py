import pandas as pd

def test_etl_source_vs_tgt_count_validation():
    # Read source data
    df_src = pd.read_csv("Data/source_data.csv")
    print("Source data is:\n", df_src)
    row_count_src = len(df_src)
    print("Source data count is:", row_count_src)

    # # Read target data
    df_tgt = pd.read_csv("Data/tgt_data.csv")
    print("Target data is:\n", df_tgt)
    row_count_tgt = len(df_tgt)
    print("Target data count is:", row_count_tgt)
    #
    # # Validation
    assert row_count_src == row_count_tgt, "Row counts do not match between source and target"
