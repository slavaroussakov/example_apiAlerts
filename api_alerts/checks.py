"""This file holds all checks as separate classes for usage in CheckFactory"""
from datetime import datetime
import statistics
from repos import Repo
from result_processors import ResultProcessor


class PriceDeviationCheck():
    """Checks for 24hr price deviation away from mean"""

    def __init__(self, repo: Repo, result_processor: ResultProcessor):
        self.repo = repo
        self.result_processor = result_processor

    def execute(self, args):
        """Entry method to start check procedure"""
        response = self.repo.get_data(args.currency)
        if response.ok:
            result = self.run_check(response)
        else:
            result = self.process_error(response)

        self.result_processor.process(result)

    def run_check(self, response):
        """Actual check logic"""
        structured_response = response.json()
        changes = self.convert_changes_to_floats(
            structured_response['changes'])

        deviation = statistics.stdev(changes)
        average = statistics.mean(changes)
        current_price = float(structured_response['close'])

        return {
            "timestamp": self.convert_timestamp(response.headers['Date']),
            "level": "INFO",
            "trading_pair": structured_response['symbol'].lower(),
            "deviation": True if abs(average - current_price) > deviation else False,
            "data": {
                "last_price": current_price,
                "average": average,
                "change": deviation,
                "sdev": deviation / average * 100
            }
        }

    def process_error(self, response):
        """Processes errors based on HTTP status"""
        return {
            "timestamp": self.convert_timestamp(response.headers['Date']),
            "level": "ERROR",
            "status_code": response.status_code,
            "failure_reason": response.json()['reason'],
            "failure_message": response.json()['message']
        }

    def convert_changes_to_floats(self, changes):
        """Helper method to convert list of strings to floats"""
        return list(map(float, changes))

    def convert_timestamp(self, timestamp):
        """Converts timestamp from repo to ISO8601 with timezone"""
        return datetime \
            .strptime(timestamp, '%a, %d %b %Y %H:%M:%S %Z') \
            .astimezone().replace(microsecond=0).isoformat()
