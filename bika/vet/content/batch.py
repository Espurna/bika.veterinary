from Products.Archetypes.public import *
from zope.component import adapts
from zope.interface import implements
from bika.lims.fields import ExtIntegerField
from bika.lims.interfaces import IBatch
from bika.health import bikaMessageFactory as _
from bika.vet.interfaces import IBatchVet
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender

class BatchVet(object):
    # This extender will apply to all Archetypes based content
    adapts(IBatch)
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
        return schematas

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
