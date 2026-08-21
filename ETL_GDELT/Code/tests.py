import Extract
import Transform
import Load

if __name__ == "__main__":

     # Initialize BigQuery client
    project_id = "prueba-505900"  # Replace with your project ID
    dataset_id="gdelt_pipeline"
    table="events"
    # Define parameters for data extraction
    PartionTime_init = "2026-08-16"
    PartionTime_end = "2026-08-17"
    Limit = 10000  # Limit of records to extract from GDELT
        
    # ETL
    print("*************************************************")
    print("Extrayendo datos ..")
    Extract.Main_Extract(project_id, PartionTime_init, PartionTime_end, Limit)
    print("*************************************************")
    print("Transformando datos ....")
    Transform.transform_data()
    print("*************************************************")
    print("Cargando datos ......")
    Load.MainLoad(project_id,bigquery=True)
    
