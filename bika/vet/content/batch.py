from Products.Archetypes.public import *
from zope.component import adapts
from zope.interface import implements
from plone.indexer.decorator import indexer
from bika.lims.fields import ExtIntegerField
from bika.lims.interfaces import IBatch
from bika.health import bikaMessageFactory as _
from bika.health.interfaces import IBatchHealth
from bika.vet.interfaces import IBatchVet, IBikaVet
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender, ISchemaModifier

from Products.Archetypes import atapi

from bika.lims.config import PROJECTNAME as BIKALIMS_PROJECTNAME
from bika.lims.content.batch import Batch as BaseBatch

class BatchVet(object):
    # This extender will apply to all Archetypes based content
    adapts(IBatchHealth)
    #adapts(IOrderableSchemaExtender)
    implements(IOrderableSchemaExtender, IBatchVet)
    #layer = IBikaVet
    fields = [
        ExtIntegerField('AAAAA',
            required = 0,
            widget=IntegerWidget(
                label=_('AAAAAA'),
            ),
        ),
    ]

    def getOrder(self, schematas):
        schematas['default'] = ['id',
                                'title',
                                'description',
                                'BatchID',
                                'ClientPatientID',
                                'Patient',
                                'AAAAA',
                                # 'PatientID',
                                # 'PatientUID',
                                # 'PatientTitle',
                                'Client',
                                # 'ClientID',
                                # 'ClientUID',
                                # 'ClientTitle',
                                'ClientBatchID',
                                'Doctor',
                                # 'DoctorID',
                                # 'DoctorUID',
                                # 'DoctorTitle',
                                'BatchDate',
                                'OnsetDate',
                                'PatientAgeAtCaseOnsetDate',
                                'OnsetDateEstimated',
                                'HoursFasting',
                                'PatientCondition',
                                'BasalBodyTemperature',
                                'MenstrualStatus',
                                'Symptoms',
                                'ProvisionalDiagnosis',
                                'CaseStatus',
                                'CaseOutcome',
                                'AetiologicAgents',
                                'AdditionalNotes',
                                'Remarks',
                                'PatientBirthDate',
                                'BatchLabels',
                                'InheritedObjects',
                                'InheritedObjectsUI',]
        import pdb;pdb.set_trace()
        return schematas

    def __init__(self, context):
        import pdb;pdb.set_trace()
        self.context = context

    def getFields(self):
        import pdb;pdb.set_trace()
        return self.fields
    #fields = [
    #ExtBooleanField('AAAAAAAAAAA',
    #default=False,
    #widget=BooleanWidget(
    #label = _("AAAAAAAAAAA"),
    #),
    #),
    #]


#class BatchVet(BaseBatch):
#    """ Inherits from bika.content.analysisspec.AnalysisSpec
#    """
#    pass

#atapi.registerType(BatchVet, BIKALIMS_PROJECTNAME)

