# from Zope2.App import zcml
# from Products.Five import fiveconfigure

# from Testing import ZopeTestCase as ztc

# from Products.PloneTestCase import PloneTestCase as ptc
# from Products.PloneTestCase.layer import onsetup


# @onsetup
# def setup_product():
#     """Set up additional products and ZCML required to test this product.

#     The @onsetup decorator causes the execution of this body to be deferred
#     until the setup of the Plone site testing layer.
#     """

#     # Load the ZCML configuration for this package and its dependencies

#     fiveconfigure.debug_mode = True
#     import rer.portlet.advanced_static

#     zcml.load_config("configure.zcml", rer.portlet.advanced_static)
#     fiveconfigure.debug_mode = False

#     # We need to tell the testing framework that these products
#     # should be available. This can't happen until after we have loaded
#     # the ZCML.

#     ztc.installPackage("rer.portlet.advanced_static")


# # The order here is important: We first call the deferred function and then
# # let PloneTestCase install it during Plone site setup

# setup_product()
# ptc.setupPloneSite(products=["rer.portlet.advanced_static"])


# class TestCase(ptc.PloneTestCase):
#     """Base class used for test cases
#     """


# class FunctionalTestCase(ptc.FunctionalTestCase):
#     """Test case class used for functional (doc-)tests
#     """
# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import rer.portlet.advanced_static


class RerPortletAdvancedStaticLayer(PloneSandboxLayer):
    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=rer.portlet.advanced_static)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "rer.portlet.advanced_static:default")


RER_PORTLET_ADVANDED_STATIC_FIXTURE = RerPortletAdvancedStaticLayer()


RER_PORTLET_ADVANDED_STATIC_INTEGRATION_TESTING = IntegrationTesting(
    bases=(RER_PORTLET_ADVANDED_STATIC_FIXTURE,),
    name="RerPortletAdvancedStaticLayer:IntegrationTesting",
)
