"""
This lambda function retrieves ssm paramaters based on
text and age; older than specified age, lambd deletes..
"""
import logging
import delete_parameters as dp
SSM_LIMIT = 10
AGE = int(0)

PARAM_FILTERS = ["test"]
LOG = logging.getLogger()
LOG.setLevel(logging.INFO)


def lambda_handler(event=None, context=None):
    """ Main """
    if 'PARAM_FILTERS' not in globals() or not PARAM_FILTERS:
        print("Empty parameter query text..exiting.")
        return
    ssm_describe_results = dp.describe_parameters(PARAM_FILTERS)
    if ssm_describe_results:
        print("Found {} parameters". format(
            len(ssm_describe_results.keys())))
        delete_candidates = dp.modify_parameter_dates(ssm_describe_results, AGE)
        if delete_candidates:
            print("{} out of {} Parameters were marked for deletion\n".format(
                len(delete_candidates), len(ssm_describe_results.keys())))
            if len(delete_candidates) > SSM_LIMIT:
                while len(delete_candidates) > SSM_LIMIT:
                    print(dp.delete_parameters(delete_candidates[:SSM_LIMIT]))
                    del delete_candidates[:SSM_LIMIT]
                print(dp.delete_parameters(delete_candidates))
            print(dp.delete_parameters(delete_candidates))
            return
        print("No parameters older than {} day/s to delete".format(AGE))
        return
    print("No SSM parameters with filter {} were found to delete".format(PARAM_FILTERS))
if __name__ == "__main__":
    lambda_handler()
