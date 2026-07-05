from src.analytics.analytics_repository import (
    AnalyticsRepository
)


class AnalyticsManager:

    def __init__(self):

        self.repository = (
            AnalyticsRepository()
        )

    def get_dashboard(
        self
    ) -> dict:

        total_jobs = (
            self.repository.get_total_jobs()
        )

        failed_jobs = (
            self.repository.get_failed_jobs()
        )

        pending_jobs = (
            self.repository.get_pending_jobs()
        )

        if total_jobs == 0:

            success_rate = 100.0

        else:

            success_rate = round(
                (
                    (
                        total_jobs - failed_jobs
                    ) / total_jobs
                ) * 100,
                2
            )

        if failed_jobs == 0:

            system_health = "HEALTHY"

        elif failed_jobs < 5:

            system_health = "WARNING"

        else:

            system_health = "CRITICAL"

        if pending_jobs == 0:

            queue_status = "IDLE"

        else:

            queue_status = "PROCESSING"

        return {

            "total_documents":
                self.repository.get_total_documents(),

            "total_chunks":
                self.repository.get_total_chunks(),

            "total_jobs":
                total_jobs,

            "failed_jobs":
                failed_jobs,

            "pending_jobs":
                pending_jobs,

            "total_uploads":
                self.repository.get_total_uploads(),

            "total_searches":
                self.repository.get_total_searches(),

            "average_search_time":
                self.repository.get_average_search_time(),

            "success_rate":
                success_rate,

            "system_health":
                system_health,

            "queue_status":
                queue_status
        }