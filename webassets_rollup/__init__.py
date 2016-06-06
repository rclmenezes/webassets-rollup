from webassets.filter import ExternalTool, option

__all__ = ['Rollup']


class Rollup(ExternalTool):
    """Use Rollup to bundle assets.

    Requires the Rollup executable to be available externally. You can
    install it using `Node Package Manager <http://npmjs.org/>`_::

        $ npm install -g rollup

    Supported configuration options:

    ROLLUP_BIN
        The path to the Rollup binary. If not set, assumes ``rollup``
        is in the system path.

    ROLLUP_EXTRA_ARGS
        A list of any additional command-line arguments.

    """

    name = 'rollup'
    max_debug_level = None
    options = {
        'binary': 'ROLLUP_BIN',
        'extra_args': option('ROLLUP_EXTRA_ARGS', type=list)
    }

    def input(self, infile, outfile, **kwargs):
        args = [self.binary or 'rollup']

        if self.extra_args:
            args.extend(self.extra_args)

        args.append(kwargs['source_path'])

        self.subprocess(args, outfile, infile)
