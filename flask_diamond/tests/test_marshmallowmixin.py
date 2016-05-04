# -*- coding: utf-8 -*-
# Flask-Diamond (c) Ian Dennis Miller

from nose.plugins.attrib import attr
from .mixins import DiamondTestCase
from .fixtures import Planet, Satellite, typical_workflow


class MarshmallowMixinTestCase(DiamondTestCase):
    "Coverage for CRUD Mixin"

    def setUp(self):
        super(MarshmallowMixinTestCase, self).setUp()
        typical_workflow()

    def test_dump(self):
        "test Marshmallow Mixin dump()"
        earth = Planet.find(name="Earth")
        result = earth.dump()
        self.assertEqual(result['name'], "Earth")

    @attr("single")
    def test_dumps(self):
        "test Marshmallow Mixin dumps()"
        moon = Satellite.find(name="Moon")
        result = moon.dumps()
        self.assertRegexpMatches(result, r"Moon")

        earth = Planet.find(name="Earth")
        result = earth.dumps()
        self.assertRegexpMatches(result, r"Moon")
        self.assertRegexpMatches(result, r"Earth")

    @attr("skip")
    def test_dumpf(self):
        pass
