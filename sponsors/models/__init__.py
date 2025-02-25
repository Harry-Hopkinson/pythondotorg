"""
Python.org sponsors app is heavily db-oriented. This results in
a huge models.py. To reduce file length the models are being
structured as a python package.
"""

from .assets import GenericAsset, ImgAsset, TextAsset, FileAsset, ResponseAsset
from .notifications import SponsorEmailNotificationTemplate, SPONSOR_TEMPLATE_HELP_TEXT
from .sponsors import Sponsor, SponsorContact, SponsorBenefit
from .benefits import BaseLogoPlacement, BaseTieredQuantity, BaseEmailTargetable, BenefitFeatureConfiguration, \
    LogoPlacementConfiguration, TieredQuantityConfiguration, EmailTargetableConfiguration, BenefitFeature, \
    LogoPlacement, EmailTargetable, TieredQuantity, RequiredImgAsset, RequiredImgAssetConfiguration, \
    RequiredTextAssetConfiguration, RequiredTextAsset, RequiredResponseAssetConfiguration, RequiredResponseAsset, \
    ProvidedTextAssetConfiguration, ProvidedTextAsset, ProvidedFileAssetConfiguration, ProvidedFileAsset
from .sponsorship import Sponsorship, SponsorshipProgram, SponsorshipBenefit, Sponsorship, SponsorshipPackage
from .contract import LegalClause, Contract, signed_contract_random_path
