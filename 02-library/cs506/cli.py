import argparse
import pkg_resources
import sys
import logging
import traceback

from cs506 import kmeans,read

def main():
    """Generate the CLI bits
    """
    try:
        parser = _CliParser()
        parser.parse()
    except Exception as e:  # Exception raised to CLI should not be thrown to users,
        logger = logging.getLogger(__name__)
        logger.debug("Exit traceback: %s", traceback.format_exc())
        sys.exit(str(e))    # it should just be captured by logs


class _CliParser():
    """Class that generates the command line bits for the kmeans cli tool
    """

    def __init__(self):
        pass

    def parse(self):
        """Parse generates and evaluates the command level parser
        """
        parser = argparse.ArgumentParser(
            description='Run some clustering algorithms')

        try:
            __version__ = pkg_resources.get_distribution('clustering').version
        except Exception:
            __version__ = 'unknown'

        parser.add_argument(
            '-v', '--version',
            help='Show the current version of clustering package',
            action='version', version=__version__)
        parser.add_argument(
            '--verbose', dest='verbose',
            help="Provide detailed logs",
            action='store_true', default=False)

        subparsers = parser.add_subparsers(title='subcommands')

        kmeans_parser = subparsers.add_parser(
            'kmeans',
            help='Cluster dataset using kmeans.',
            description='Cluster dataset using Lloyd\'s algo for kmeans.')
        kmeans_parser.add_argument(
            'dataset',
            help="path to a dataset")
        kmeans_parser.add_argument(
            'k',
            help="the number of clusters")
        kmeans_parser.set_defaults(func=self.kmeans)

        args = parser.parse_args()
        logging.basicConfig(
            level=logging.DEBUG if args.verbose else logging.WARNING
        )

        func = getattr(args, 'func', None)
        if callable(func):
            func(args)
        else:
            parser.print_help(sys.stderr)
            sys.exit(2)

    def kmeans_template(self, args, func):
        """Run the kmeans command
        """
        import csv
        dataset = read.read_csv(args.dataset_file)
        clustering = func(dataset=dataset, k=int(args.k))
        cost = kmeans.cost_function(clustering)

        for _ in range(100):
            new_clustering = func(dataset=dataset, k=int(args.k))
            new_cost = kmeans.cost_function(clustering)
            if new_cost < cost:
                clustering = new_clustering
                cost = new_cost

        for assignment in clustering.keys():
            file_name = str(args.dataset).split(".")[0]+"_k_is_"+args.k+"_"+str(assignment)+".csv"
            with open(file_name, "w") as f:
                writer = csv.writer(f)
                print("assignement ", assignment, " is: ", clustering[assignment])
                writer.writerows(clustering[assignment])
            f.close()

    def kmeans(self, args, func=kmeans_template):
        func(self, args, kmeans.k_means)

    def kmeans_pp(self, args, func=kmeans_template):
        func(self, args, kmeans.k_means_pp)
