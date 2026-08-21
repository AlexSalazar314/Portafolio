import Extract 
import Transform
def main():
 # Initialize BigQuery client


    project_id = "prueba-505900"  # Replace with your project ID
        
    # Define parameters for data extraction
    PartionTime_init = "2026-08-16"
    PartionTime_end = "2026-08-17"
    Limit = 10  # Limit of records to extract from GDELT
        
    # Extract data from GDELT
    df,events,country = Extract.Main_Extract(project_id, PartionTime_init, PartionTime_end, Limit)
    df=Transform.transform_data(df,events,country)


    
    # Print the extracted data information
    print(df.head())

if __name__ == "__main__":
    main()
