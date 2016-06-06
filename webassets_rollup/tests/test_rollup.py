from unittest import TestCase

from webassets.filter import register_filter
from webassets.test import TempEnvironmentHelper

from webassets_rollup import Rollup


register_filter(Rollup)


class RollupFilterTestCase(TempEnvironmentHelper, TestCase):
    default_files = {
        'main.js': 'import { cube } from "./maths.js"; console.log(cube(5));',
        'maths.js': 'export function cube ( x ) { return x * x * x; }'
    }

    def setUp(self):
        super(RollupFilterTestCase, self).setup()

    def test_rollup_filter(self):
        self.mkbundle('main.js', filters='rollup', output='bundle.js').build()
        assert 'cube(5)' in self.get('bundle.js')
