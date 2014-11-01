# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'

from .. import gedcomx_enum

ConfidenceLevel = gedcomx_enum(
    HIGH=u"http://gedcomx.org/High",
    MEDIUM=u"http://gedcomx.org/Medium",
    LOW=u"http://gedcomx.org/Low")
"""Enumerations of levels of confidence

    :ivar HIGH: High confidence
    :ivar MEDIUM: Medium confidence
    :ivar LOW: Low confidence"""

DocumentType = gedcomx_enum(
    Abstract=u"http://gedcomx.org/Abstract",
    Translation=u"http://gedcomx.org/Translation",
    Transcription=u"http://gedcomx.org/Transcription",
    Analysis=u"http://gedcomx.org/Analysis"
)
"""Enumeration of document types.

    :ivar Abstract: The document is an abstract of a record or a document.
    :ivar Translation: The document is a translation of a record or a document.
    :ivar Transcription: The document is a transcription (full or partial) of a record or document.
    :ivar Analysis: The document is an analysis done by a researcher, often used as a genealogical proof statement.
"""

EventRoleType = gedcomx_enum(
    Principal=u"http://gedcomx.org/Principal",
    Participant=u"http://gedcomx.org/Participant",
    Official=u"http://gedcomx.org/Official",
    Witness=u"http://gedcomx.org/Witness"
)
"""Enumeration of standard event roles."""

EventType = gedcomx_enum(
    Adoption=u"http://gedcomx.org/Adoption",
    Adultchristening=u"http://gedcomx.org/AdultChristening",
    Annulment=u"http://gedcomx.org/Annulment",
    Baptism=u"http://gedcomx.org/Baptism",
    Barmitzvah=u"http://gedcomx.org/BarMitzvah",
    Batmitzvah=u"http://gedcomx.org/BatMitzvah",
    Birth=u"http://gedcomx.org/Birth",
    Blessing=u"http://gedcomx.org/Blessing",
    Burial=u"http://gedcomx.org/Burial",
    Census=u"http://gedcomx.org/Census",
    Christening=u"http://gedcomx.org/Christening",
    Circumcision=u"http://gedcomx.org/Circumcision",
    Confirmation=u"http://gedcomx.org/Confirmation",
    Cremation=u"http://gedcomx.org/Cremation",
    Death=u"http://gedcomx.org/Death",
    Divorce=u"http://gedcomx.org/Divorce",
    Divorcefiling=u"http://gedcomx.org/DivorceFiling",
    Education=u"http://gedcomx.org/Education",
    Engagement=u"http://gedcomx.org/Engagement",
    Emigration=u"http://gedcomx.org/Emigration",
    Excommunication=u"http://gedcomx.org/Excommunication",
    Firstcommunion=u"http://gedcomx.org/FirstCommunion",
    Funeral=u"http://gedcomx.org/Funeral",
    Immigration=u"http://gedcomx.org/Immigration",
    Landtransaction=u"http://gedcomx.org/LandTransaction",
    Marriage=u"http://gedcomx.org/Marriage",
    Militaryaward=u"http://gedcomx.org/MilitaryAward",
    Militarydischarge=u"http://gedcomx.org/MilitaryDischarge",
    Mission=u"http://gedcomx.org/Mission",
    Movefrom=u"http://gedcomx.org/MoveFrom",
    Moveto=u"http://gedcomx.org/MoveTo",
    Naturalization=u"http://gedcomx.org/Naturalization",
    Ordination=u"http://gedcomx.org/Ordination",
    Retirement=u"http://gedcomx.org/Retirement"
)
"""Enumeration of standard event types

:ivar Adoption: An adoption event.
:ivar Adultchristening: An adult christening event.
:ivar Annulment: An annulment event of a marriage.
:ivar Baptism: A baptism event.
:ivar Barmitzvah: A bar mitzvah event.
:ivar Batmitzvah: A bat mitzvah event.
:ivar Birth: A birth event.
:ivar Blessing: An official blessing event, such as at the hands of a clergy member or at another religious rite.
:ivar Burial: A burial event.
:ivar Census: A census event.
:ivar Christening:  A christening event *at birth*. Note: use `AdultChristening` for a christening event as an adult.
:ivar Circumcision: A circumcision event.
:ivar Confirmation: A confirmation event (or other rite of initiation) in a church or religion.
:ivar Cremation: A cremation event after death.
:ivar Death: A death event.
:ivar Divorce: A divorce event.
:ivar Divorcefiling: A divorce filing event.
:ivar Education: A education or an educational achievement event (e.g. diploma, graduation, scholarship, etc.).
:ivar Engagement: An engagement to be married event.
:ivar Emigration: An emigration event.
:ivar Excommunication: An excommunication event from a church.
:ivar Firstcommunion: A first communion event.
:ivar Funeral:  A funeral event.
:ivar Immigration: An immigration event.
:ivar Landtransaction: A land transaction event.
:ivar Marriage: A marriage event.
:ivar Militaryaward: A military award event.
:ivar Militarydischarge: A military discharge event.
:ivar Mission: A mission event.
:ivar Movefrom: An event of a move (i.e. change of residence) from a location.
:ivar Moveto: An event of a move (i.e. change of residence) to a location.
:ivar Naturalization: A naturalization event (i.e. acquisition of citizenship and nationality).
:ivar Ordination: An ordination event.
:ivar Retirement: A retirement event.
"""

FacetType = gedcomx_enum(
    Year=u"http://gedcomx.org/Year",
    State=u"http://gedcomx.org/State",
    Province=u"http://gedcomx.org/Province",
    Country=u"http://gedcomx.org/Country",
    City=u"http://gedcomx.org/City",
    Parish=u"http://gedcomx.org/Parish",
    Township=u"http://gedcomx.org/Township",
    Page=u"http://gedcomx.org/Page",
    Volume=u"http://gedcomx.org/Volume",
    Date=u"http://gedcomx.org/Date",
    Place=u"http://gedcomx.org/Place",
    Name=u"http://gedcomx.org/Name",
    Gender=u"http://gedcomx.org/Gender"
)
"""Enumeration of known facet types.

:ivar Year: A Year.
:ivar State: A State.
:ivar Province: A Province.
:ivar Country: A Country.
:ivar City: A City.
:ivar Parish: A Parish.
:ivar Township: A Township.
:ivar Page: A Page.
:ivar Volume: A Volume.
:ivar Date: A Date.
:ivar Place: A Place.
:ivar Name: A Name.
:ivar Gender: A gender.
"""

FactQualifierType = gedcomx_enum(
    Age=u"http://gedcomx.org/Age",
    Cause=u"http://gedcomx.org/Cause",
    Religion=u"http://gedcomx.org/Religion"
)
"""Enumeration of standard fact qualifiers.

:ivar Age: The age of a person at the event described by the fact.
:ivar Cause: The cause of a specific fact, such as the cause of death.
:ivar Religion: The religion associated with a religious event such as a baptism or excommunication.
"""

FactType = gedcomx_enum(
    Adoption=u"http://gedcomx.org/Adoption",
    AdultChristening=u"http://gedcomx.org/AdultChristening",
    Amnesty=u"http://gedcomx.org/Amnesty",
    Apprenticeship=u"http://gedcomx.org/Apprenticeship",
    Arrest=u"http://gedcomx.org/Arrest",
    Baptism=u"http://gedcomx.org/Baptism",
    BarMitzvah=u"http://gedcomx.org/BarMitzvah",
    BatMitzvah=u"http://gedcomx.org/BatMitzvah",
    Birth=u"http://gedcomx.org/Birth",
    Blessing=u"http://gedcomx.org/Blessing",
    Burial=u"http://gedcomx.org/Burial",
    Caste=u"http://gedcomx.org/Caste",
    Census=u"http://gedcomx.org/Census",
    Christening=u"http://gedcomx.org/Christening",
    Circumcision=u"http://gedcomx.org/Circumcision",
    Clan=u"http://gedcomx.org/Clan",
    Confirmation=u"http://gedcomx.org/Confirmation",
    Cremation=u"http://gedcomx.org/Cremation",
    Death=u"http://gedcomx.org/Death",
    Education=u"http://gedcomx.org/Education",
    EducationEnrollment=u"http://gedcomx.org/EducationEnrollment",
    Emigration=u"http://gedcomx.org/Emigration",
    Ethnicity=u"http://gedcomx.org/Ethnicity",
    Excommunication=u"http://gedcomx.org/Excommunication",
    FirstCommunion=u"http://gedcomx.org/FirstCommunion",
    Funeral=u"http://gedcomx.org/Funeral",
    GenderChange=u"http://gedcomx.org/GenderChange",
    Graduation=u"http://gedcomx.org/Graduation",
    Immigration=u"http://gedcomx.org/Immigration",
    Imprisonment=u"http://gedcomx.org/Imprisonment",
    LandTransaction=u"http://gedcomx.org/LandTransaction",
    Language=u"http://gedcomx.org/Language",
    Living=u"http://gedcomx.org/Living",
    MaritalStatus=u"http://gedcomx.org/MaritalStatus",
    Medical=u"http://gedcomx.org/Medical",
    MilitaryAward=u"http://gedcomx.org/MilitaryAward",
    MilitaryDischarge=u"http://gedcomx.org/MilitaryDischarge",
    MilitaryDraftRegistration=u"http://gedcomx.org/MilitaryDraftRegistration",
    MilitaryInduction=u"http://gedcomx.org/MilitaryInduction",
    MilitaryService=u"http://gedcomx.org/MilitaryService",
    Mission=u"http://gedcomx.org/Mission",
    MoveFrom=u"http://gedcomx.org/MoveFrom",
    MoveTo=u"http://gedcomx.org/MoveTo",
    MultipleBirth=u"http://gedcomx.org/MultipleBirth",
    NationalId=u"http://gedcomx.org/NationalId",
    Nationality=u"http://gedcomx.org/Nationality",
    Naturalization=u"http://gedcomx.org/Naturalization",
    NumberOfMarriages=u"http://gedcomx.org/NumberOfMarriages",
    Occupation=u"http://gedcomx.org/Occupation",
    Ordination=u"http://gedcomx.org/Ordination",
    Pardon=u"http://gedcomx.org/Pardon",
    PhysicalDescription=u"http://gedcomx.org/PhysicalDescription",
    Probate=u"http://gedcomx.org/Probate",
    Property=u"http://gedcomx.org/Property",
    Religion=u"http://gedcomx.org/Religion",
    Residence=u"http://gedcomx.org/Residence",
    Retirement=u"http://gedcomx.org/Retirement",
    Stillbirth=u"http://gedcomx.org/Stillbirth",
    TaxAssessment=u"http://gedcomx.org/TaxAssessment",
    Will=u"http://gedcomx.org/Will",
    Visit=u"http://gedcomx.org/Visit",
    Yahrzeit=u"http://gedcomx.org/Yahrzeit",
    Annulment=u"http://gedcomx.org/Annulment",
    CommonLawMarriage=u"http://gedcomx.org/CommonLawMarriage",
    CivilUnion=u"http://gedcomx.org/CivilUnion",
    Divorce=u"http://gedcomx.org/Divorce",
    DivorceFiling=u"http://gedcomx.org/DivorceFiling",
    DomesticPartnership=u"http://gedcomx.org/DomesticPartnership",
    Engagement=u"http://gedcomx.org/Engagement",
    Marriage=u"http://gedcomx.org/Marriage",
    MarriageBanns=u"http://gedcomx.org/MarriageBanns",
    MarriageContract=u"http://gedcomx.org/MarriageContract",
    MarriageLicense=u"http://gedcomx.org/MarriageLicense",
    MarriageNotice=u"http://gedcomx.org/MarriageNotice",
    NumberOfChildren=u"http://gedcomx.org/NumberOfChildren",
    Separation=u"http://gedcomx.org/Separation",
    AdoptiveParent=u"http://gedcomx.org/AdoptiveParent",
    BiologicalParent=u"http://gedcomx.org/BiologicalParent",
    FosterParent=u"http://gedcomx.org/FosterParent",
    GuardianParent=u"http://gedcomx.org/GuardianParent",
    StepParent=u"http://gedcomx.org/StepParent"
)
"""Enumeration of standard fact types.

Facts generally applicable within the scope of a person.

:ivar Adoption: A fact of a person's adoption. In the context of a parent-child relationship, it describes a fact of the
                adoption of a child by a parent.
:ivar Adultchristening: A fact of a person's christening as an adult.
:ivar Amnesty: A fact of a person's amnesty.
:ivar Apprenticeship: A fact of a person's apprenticeship.
:ivar Arrest: A fact of a person's arrest.
:ivar Baptism: A fact of a person's baptism.
:ivar Barmitzvah: A fact of a person's bar mitzvah.
:ivar Batmitzvah: A fact of a person's bat mitzvah.
:ivar Birth: A fact of a person's birth.
:ivar Blessing: A fact of an official blessing received by a person, such as at the hands of a clergy member or at
                another religious rite.
:ivar Burial: A fact of the burial of person's body after death.
:ivar Caste: A fact of a person's caste.
:ivar Census: A fact of a person's participation in a census.
:ivar Christening: A fact of a person's christening *at birth*. Note: use `AdultChristening` for the christening as an
                   adult.
:ivar Circumcision: A fact of a person's circumcision.
:ivar Clan: A fact of a person's clan.
:ivar Confirmation: A fact of a person's confirmation (or other rite of initiation) in a church or religion.
:ivar Cremation: A fact of the cremation of person's body after death.
:ivar Death: A fact of the death of a person.
:ivar Education: A fact of an education of a person.
:ivar Educationenrollment: A fact of a person's enrollment in an educational program or institution.
:ivar Emigration: A fact of the emigration of a person.
:ivar Ethnicity: A fact of a person's ethnicity or race.
:ivar Excommunication: A fact of a person's excommunication from a church.
:ivar Firstcommunion: A fact of a person's first communion in a church.
:ivar Funeral: A fact of a person's funeral.
:ivar Genderchange: A fact of a person's gender change.
:ivar Graduation: A fact of a person's graduation from a scholastic institution.
:ivar Immigration: A fact of a person's immigration.
:ivar Imprisonment: A fact of a person's imprisonment.
:ivar Landtransaction: A fact of a land transaction enacted by a person.
:ivar Language: A fact of a language spoken by a person.
:ivar Living: A fact of a record of a person's living for a specific period. This is designed to include "flourish",
              defined to mean the time period in an adult's life where he was most productive, perhaps as a writer or
              member of the state assembly. It does not reflect the person's birth and death dates.
:ivar Maritalstatus: A fact of a person's marital status.
:ivar Medical: A fact of a person's medical record, such as for an illness or hospital stay.
:ivar Militaryaward: A fact of a person's military award.
:ivar Militarydischarge: A fact of a person's military discharge.
:ivar Militarydraftregistration: A fact of a person's registration for a military draft.
:ivar Militaryinduction: A fact of a person's military induction.
:ivar Militaryservice: A fact of a person's militray service.
:ivar Mission: A fact of a person's church mission.
:ivar Movefrom: A fact of a person's move (i.e. change of residence) from a location.
:ivar Moveto: A fact of a person's move (i.e. change of residence) to a new location.
:ivar Multiplebirth: A fact that a person was born as part of a multiple birth (e.g. twin, triplet, etc.)
:ivar Nationalid: A fact of a person's national id (e.g. social security number).
:ivar Nationality: A fact of a person's nationality.
:ivar Naturalization: A fact of a person's naturalization (i.e. acquisition of citizenship and nationality).
:ivar Numberofmarriages: A fact of a person's number of marriages.
:ivar Occupation: A fact of a person's occupation or employment.
:ivar Ordination: A fact of a person's ordination to a stewardship in a church.
:ivar Pardon: A fact of a person's legal pardon.
:ivar Physicaldescription: A fact of a person's physical description.
:ivar Probate: A fact of a receipt of probate of a person's property.
:ivar Property: A fact of a person's property or possessions.
:ivar Religion: A fact of a person's religion.
:ivar Residence: A fact of a person's residence.
:ivar Retirement: A fact of a person's retirement.
:ivar Stillbirth: A fact of a person's stillbirth.
:ivar Taxassessment: A fact of a person's tax assessment.
:ivar Will: A fact of a person's will.
:ivar Visit: A fact of a person's visit to a place different from the person's residence.
:ivar Yahrzeit: A fact of a person's _yahrzeit_ date.  A person's yahzeit is the anniversary of their death as measured
                by the Hebrew calendar.

Facts generally applicable within the scope of a couple

:ivar Annulment: The fact of an annulment of a marriage.
:ivar Commonlawmarriage: The fact of a marriage by common law.
:ivar Civilunion: The fact of a civil union.
:ivar Divorce: The fact of a divorce of a couple.
:ivar Divorcefiling: The fact of a filing for divorce.
:ivar Domesticpartnership: The fact of a domestic partnership.
:ivar Engagement: The fact of an engagement to be married.
:ivar Marriage: The fact of a marriage.
:ivar Marriagebanns: The fact of a marriage banns.
:ivar Marriagecontract: The fact of a marriage contract.
:ivar Marriagelicense: The fact of a marriage license.
:ivar Marriagenotice: The fact of a marriage notice.
:ivar Numberofchildren: A fact of the number of children of a person or relationship.
:ivar Separation: A fact of a couple's separation.

Facts generally applicable within the scope of a parent-child relationship.

:ivar Adoptiveparent: A fact about an adoptive relationship between a parent an a child.
:ivar Biologicalparent: A fact the biological relationship between a parent and a child.
:ivar Fosterparent: A fact about a foster relationship between a foster parent and a child.
:ivar Guardianparent: A fact about a legal guardianship between a parent and a child.
:ivar Stepparent: A fact about the step relationship between a parent and a child.
:ivar Sociologicalparent: A fact about a sociological relationship between a parent and a child, but not definable in
                          typical legal or biological terms.
"""

FieldType = gedcomx_enum(
    Age=u"http://gedcomx.org/Age",
    Date=u"http://gedcomx.org/Date",
    Place=u"http://gedcomx.org/Place",
    Gender=u"http://gedcomx.org/Gender",
    Name=u"http://gedcomx.org/Name",
    Role=u"http://gedcomx.org/Role",
    Years=u"http://gedcomx.org/Years",
    Months=u"http://gedcomx.org/Months",
    Days=u"http://gedcomx.org/Days",
    Hours=u"http://gedcomx.org/Hours",
    Minutes=u"http://gedcomx.org/Minutes",
    Year=u"http://gedcomx.org/Year",
    Month=u"http://gedcomx.org/Month",
    Day=u"http://gedcomx.org/Day",
    Hour=u"http://gedcomx.org/Hour",
    Minute=u"http://gedcomx.org/Minute",
    Address=u"http://gedcomx.org/Address",
    Cemetery=u"http://gedcomx.org/Cemetery",
    City=u"http://gedcomx.org/City",
    Church=u"http://gedcomx.org/Church",
    County=u"http://gedcomx.org/County",
    Country=u"http://gedcomx.org/Country",
    District=u"http://gedcomx.org/District",
    Hospital=u"http://gedcomx.org/Hospital",
    Island=u"http://gedcomx.org/Island",
    MilitaryBase=u"http://gedcomx.org/MilitaryBase",
    Mortuary=u"http://gedcomx.org/Mortuary",
    Parish=u"http://gedcomx.org/Parish",
    PlotNumber=u"http://gedcomx.org/PlotNumber",
    PostOffice=u"http://gedcomx.org/PostOffice",
    PostalCode=u"http://gedcomx.org/PostalCode",
    Prison=u"http://gedcomx.org/Prison",
    Province=u"http://gedcomx.org/Province",
    Section=u"http://gedcomx.org/Section",
    Ship=u"http://gedcomx.org/Ship",
    State=u"http://gedcomx.org/State",
    Territory=u"http://gedcomx.org/Territory",
    Town=u"http://gedcomx.org/Town",
    Township=u"http://gedcomx.org/Township",
    Ward=u"http://gedcomx.org/Ward",
    Prefix=u"http://gedcomx.org/Prefix",
    Suffix=u"http://gedcomx.org/Suffix",
    Given=u"http://gedcomx.org/Given",
    Surname=u"http://gedcomx.org/Surname",
    Abusua=u"http://gedcomx.org/Abusua",
    BatchNumber=u"http://gedcomx.org/BatchNumber",
    Caste=u"http://gedcomx.org/Caste",
    Clan=u"http://gedcomx.org/Clan",
    CommonLawMarriage=u"http://gedcomx.org/CommonLawMarriage",
    Education=u"http://gedcomx.org/Education",
    Ethnicity=u"http://gedcomx.org/Ethnicity",
    FatherBirthPlace=u"http://gedcomx.org/FatherBirthPlace",
    NeverHadChildren=u"http://gedcomx.org/NeverHadChildren",
    NeverMarried=u"http://gedcomx.org/NeverMarried",
    NumberOfChildren=u"http://gedcomx.org/NumberOfChildren",
    NumberOfMarriages=u"http://gedcomx.org/NumberOfMarriages",
    Household=u"http://gedcomx.org/Household",
    IsHeadOfHousehold=u"http://gedcomx.org/IsHeadOfHousehold",
    MaritalStatus=u"http://gedcomx.org/MaritalStatus",
    MotherBirthPlace=u"http://gedcomx.org/MotherBirthPlace",
    MultipleBirth=u"http://gedcomx.org/MultipleBirth",
    NameSake=u"http://gedcomx.org/NameSake",
    NationalId=u"http://gedcomx.org/NationalId",
    Nationality=u"http://gedcomx.org/Nationality",
    Occupation=u"http://gedcomx.org/Occupation",
    PhysicalDescription=u"http://gedcomx.org/PhysicalDescription",
    Property=u"http://gedcomx.org/Property",
    Race=u"http://gedcomx.org/Race",
    Religion=u"http://gedcomx.org/Religion",
    RelationshipToHead=u"http://gedcomx.org/RelationshipToHead",
    Stillbirth=u"http://gedcomx.org/Stillbirth",
    TitleOfNobility=u"http://gedcomx.org/TitleOfNobility",
    Tribe=u"http://gedcomx.org/Tribe"
)
"""Enumeration of known fields"""

FieldValueType = gedcomx_enum(
    Original=u"http://gedcomx.org/Original",
    Interpreted=u"http://gedcomx.org/Interpreted"
)
"""Enumeration of known field value types

:ivar Original: The field value is original, extracted directly from the record. What you see is what you get,
                including misspellings and other errors in the record.
:ivar Interpreted: The field value is interpreted, meaning a user or other automated process applied some reasoning to
                   interpret the value.
"""

GenderType = gedcomx_enum(
    Male=u"http://gedcomx.org/Male",
    Female=u"http://gedcomx.org/Female",
    Unknown=u"http://gedcomx.org/Unknown"
)
"""Enumeration of known gender types.

:ivar Male: Male
:ivar Female: Female.
:ivar Unknown: Unknown. Note that this should be used strictly as "unknown" and not to indicate a type that is not set
               or not understood."""


IdentifierType = gedcomx_enum(
    Primary=u"http://gedcomx.org/Primary",
    Evidence=u"http://gedcomx.org/Evidence",
    Deprecated=u"http://gedcomx.org/Deprecated",
    Persistent=u"http://gedcomx.org/Persistent"
)
"""Enumeration of standard identifier types.

:ivar Primary: The primary identifier for the resource.
:ivar Evidence: An identifier for the evidence that supports the resource. For example, when a conclusion about a
                person is extracted, analyzed and evaluated atomically within the context of a single source, it takes
                the form of a (extracted) person conclusion, and the extracted conclusion may supply an identifier for
                the person. As all evidence for the person is gathered, the (working) person conclusion identifies the
                evidence used to support the conclusion by including each evidence identifier in the list of identifiers
                for the person.
:ivar Deprecated: An identifier that has been relegated, deprecated, or otherwise downgraded. This identifier is
                  commonly used as the result of a merge when what was once a primary identifier for a person is no
                  longer primary.
:ivar Persistent: An identifier that is considered to be a long-term persistent identifier. Applications that provide
                  persistent identifiers are claiming that links to the resource using the identifier won't break.
"""

#TODO: NamePartQualifierType = gedcomx_enum()

NamePartType = gedcomx_enum(
    Prefix=u"http://gedcomx.org/Prefix",
    Suffix=u"http://gedcomx.org/Suffix",
    Given=u"http://gedcomx.org/Given",
    Surname=u"http://gedcomx.org/Surname"
)
"""Enumeration of standard name part types."""

NameType = gedcomx_enum(
    BirthName=u"http://gedcomx.org/BirthName",
    DeathName=u"http://gedcomx.org/DeathName",
    MarriedName=u"http://gedcomx.org/MarriedName",
    AlsoKnownAs=u"http://gedcomx.org/AlsoKnownAs",
    Nickname=u"http://gedcomx.org/Nickname",
    AdoptiveName=u"http://gedcomx.org/AdoptiveName",
    FormalName=u"http://gedcomx.org/FormalName",
    ReligiousName=u"http://gedcomx.org/ReligiousName"
)
"""Enumeration of standard name types.

:ivar BirthName: Name given at birth.
:ivar DeathName: Name used at the time of death.
:ivar MarriedName: Name accepted at marriage.
:ivar AlsoKnownAs: "Also known as" name.
:ivar Nickname: Nickname.
:ivar AdoptiveName: Name given at adoption.
:ivar FormalName: A formal name, usually given to distinguish it from a name more commonly used.
:ivar ReligiousName: A name given at a religious rite or ceremony.
"""

RecordType = gedcomx_enum(
    Admission=u"http://gedcomx.org/Admission",
    Adoption=u"http://gedcomx.org/Adoption",
    Affidavit=u"http://gedcomx.org/Affidavit",
    Application=u"http://gedcomx.org/Application",
    Arrival=u"http://gedcomx.org/Arrival",
    Bank=u"http://gedcomx.org/Bank",
    Baptism=u"http://gedcomx.org/Baptism",
    Birth=u"http://gedcomx.org/Birth",
    Burial=u"http://gedcomx.org/Burial",
    Business=u"http://gedcomx.org/Business",
    Cemetery=u"http://gedcomx.org/Cemetery",
    Census=u"http://gedcomx.org/Census",
    Christening=u"http://gedcomx.org/Christening",
    Confirmation=u"http://gedcomx.org/Confirmation",
    Correspondence=u"http://gedcomx.org/Correspondence",
    Death=u"http://gedcomx.org/Death",
    Departure=u"http://gedcomx.org/Departure",
    Divorce=u"http://gedcomx.org/Divorce",
    Duplicate=u"http://gedcomx.org/Duplicate",
    Draft=u"http://gedcomx.org/Draft",
    Estate=u"http://gedcomx.org/Estate",
    Index=u"http://gedcomx.org/Index",
    IntendedMarriage=u"http://gedcomx.org/IntendedMarriage",
    Land=u"http://gedcomx.org/Land",
    Legal=u"http://gedcomx.org/Legal",
    Marriage=u"http://gedcomx.org/Marriage",
    MarriageAffidavit=u"http://gedcomx.org/MarriageAffidavit",
    MarriageAmendment=u"http://gedcomx.org/MarriageAmendment",
    MarriageBanns=u"http://gedcomx.org/MarriageBanns",
    MarriageConsent=u"http://gedcomx.org/MarriageConsent",
    MarriageDuplicate=u"http://gedcomx.org/MarriageDuplicate",
    MarriageLicense=u"http://gedcomx.org/MarriageLicense",
    MarriageReturns=u"http://gedcomx.org/MarriageReturns",
    Membership=u"http://gedcomx.org/Membership",
    Migration=u"http://gedcomx.org/Migration",
    Military=u"http://gedcomx.org/Military",
    Naturalization=u"http://gedcomx.org/Naturalization",
    Passenger=u"http://gedcomx.org/Passenger",
    Pension=u"http://gedcomx.org/Pension",
    Probate=u"http://gedcomx.org/Probate",
    RelatedDocument=u"http://gedcomx.org/RelatedDocument",
    ReligiousCreeds=u"http://gedcomx.org/ReligiousCreeds",
    Roll=u"http://gedcomx.org/Roll",
    Tax=u"http://gedcomx.org/Tax",
    Vital=u"http://gedcomx.org/Vital"
)
"""Enumeration of known record types.

:ivar Admission: A record of a person's admission to an institution, society, or other association.
:ivar Adoption: A record of an adoption.
:ivar Affidavit: An affidavit.
:ivar Application: A person's application to an institution, society or other association.
:ivar Arrival: A record of a person's arrival at a certain place.
:ivar Bank: A bank record.
:ivar Baptism: A record of a person's baptism.
:ivar Birth: A record of a birth.
:ivar Burial: A record of a person's burial or interment.
:ivar Business: todo: document this type.
:ivar Cemetery: todo: document this type.
:ivar Census: A census record.
:ivar Christening: A record of a person's christening.
:ivar Confirmation: A record of a person's confirmation.
:ivar Correspondence: todo: document this type.
:ivar Death: A death record.
:ivar Departure: A record of a person's departure from a certain place.
:ivar Divorce: A divorce record.
:ivar Duplicate: todo: document this type.
:ivar Draft: A draft record.
:ivar Estate: todo: document this type.
:ivar Index: todo: document this type.
:ivar Intendedmarriage:
:ivar Land: A land record.
:ivar Legal: A legal record.
:ivar Marriage: A marriage record.
:ivar Marriageaffidavit: A marriage affidavit.
:ivar Marriageamendment: todo: document this type.
:ivar Marriagebanns: A record of a person's banns of marriage.
:ivar Marriageconsent:
:ivar Marriageduplicate: todo: document this type.
:ivar Marriagelicense: A marriage license.
:ivar Marriagereturns:
:ivar Membership:
:ivar Migration: A migration record.
:ivar Military: A military record.
:ivar Naturalization: A naturalization record.
:ivar Passenger: A passenger record.
:ivar Pension: A pension record.
:ivar Probate: A probate record.
:ivar Relateddocument: todo: document this type.
:ivar Religiouscreeds: todo: document this type.
:ivar Roll: A roll.
:ivar Tax: A tax record.
:ivar Vital: A vital record.
"""


RelationshipType = gedcomx_enum(
    Couple=u"http://gedcomx.org/Couple",
    ParentChild=u"http://gedcomx.org/ParentChild"
)
"""Enumeration of standard relationship types."""


ResourceType = gedcomx_enum(
    Record=u"http://gedcomx.org/Record",
    Collection=u"http://gedcomx.org/Collection",
    DigitalArtifact=u"http://gedcomx.org/DigitalArtifact",
    PhysicalArtifact=u"http://gedcomx.org/PhysicalArtifact",
    Person=u"http://gedcomx.org/Person"
)
"""Enumeration of high-level genealogical resource types.

:ivar Record: A historical record.
:ivar Collection: A Collection.
:ivar DigitalArtifact: A digital artifact, such as a digital image or video.
:ivar PhysicalArtifact: A physical artifact.
:ivar Person: A person.
"""

SourceReferenceQualifierType = gedcomx_enum(
    CharacterRegion=u"http://gedcomx.org/CharacterRegion",
    RectangleRegion=u"http://gedcomx.org/RectangleRegion",
    TimeRegion=u"http://gedcomx.org/TimeRegion"
)
"""Enumeration of standard source reference qualifiers.

:ivar CharacterRegion: A region of text in a digital document, in the form of `a,b` where `a` is the start character
                       and `b` is the end character.
:ivar RectangleRegion: A rectangular region of a digital image. The value of the qualifier is interpreted as a series
                       of four comma-separated numbers. If all of the numbers is less than 1, the value is interpreted
                       in the form of `x1,y1,x2,y2` where `x1,y1` is the relative percentage-based coordinates of the
                       top-left corner of the rectangle and `x2,y2` is the relative percentage-based coordinates of the
                       bottom-right corner of the rectangle. If any of the numbers is more than 1, the value is
                       interpreted in the form of `x,y,w,h` where `x` is the point on the X axis of the image in pixels,
                       `y` is the point on the Y axis in pixels, `w` is the width of the rectangle in pixels, and `h`
                       in the height of the rectangle in pixels.
:ivar TimeRegion: A region of time of an audio or video recording, in the form of `a,b` where `a` is the starting point
                  in milliseconds and `b` is the ending point in milliseconds.
"""
