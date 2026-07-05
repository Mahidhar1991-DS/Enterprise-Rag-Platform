from src.database.postgres_client import (
    DatabaseClient
)

from src.constants.job_status import (
    JobStatus
)

from src.constants.metric_names import (
    MetricNames
)

class AnalyticsRepository:

    def __init__(self):

        self.db = DatabaseClient()

    def get_total_documents(
        self
    ) -> int:

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                select count(*)
                from documents
                """
            )

            return cursor.fetchone()[0]

        finally:

            conn.close()
    
    def get_total_chunks(
        self
    ) -> int:
        conn = self.db.get_connection()
        
        try:
            
            cursor = conn.execute(
                """select count(*)
                from document_chunks
                """
            )   
            
            return cursor.fetchone()[0]
        finally:

            conn.close()     
    
    def get_total_jobs(
        self
    ) -> int:
        
        conn = self.db.get_connection()
        
        try:
            
            cursor = conn.execute(
                """select count(*)
                from jobs"""
            )
            
            return cursor.fetchone()[0]
        finally:
            
            conn.close()
    
    def get_failed_jobs(
        self
    ) -> int:
        
        conn = self.db.get_connection()
        
        try:
            
            cursor = conn.execute(
                """select count(*)
                from jobs
                where status = ?
                """,
                (JobStatus.FAILED,)
            )
            return cursor.fetchone()[0]
        finally:

            conn.close()
            
    
    def get_pending_jobs(
        self
    ) -> int:
        
        conn = self.db.get_connection()
        
        try:
            
            cursor = conn.execute(
                """select count(*) 
                from jobs
                where status = ?
                """,
                (JobStatus.PENDING,)
            )
            
            return cursor.fetchone()[0]
        finally:

            conn.close()
    
    def get_total_uploads(
        self
    ) -> int:
        
        conn = self.db.get_connection()
        
        try:
            
            cursor = conn.execute(
                """
                select count(*)
                from metrics
                where metric_name = ?
                """,
                (MetricNames.UPLOAD,)
            )
            return cursor.fetchone()[0]
        finally:

            conn.close()
    
    def get_total_searches(
        self
    ) -> int:
        
        conn = self.db.get_connection()
        
        try:
            
            cursor = conn.execute(
                """
                select count(*)
                from metrics
                where metric_name = ?
                """,
                (MetricNames.SEARCH,)
            )
            return cursor.fetchone()[0] 
    
        finally:

            conn.close()
    
    def get_average_search_time(
        self
    ) -> float:

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT AVG(metric_value)
                FROM metrics
                WHERE metric_name = ?
                """,
                (
                    MetricNames.SEARCH_TIME,
                )
            )

            result = cursor.fetchone()[0]

            return result if result else 0.0

        finally:

            conn.close()