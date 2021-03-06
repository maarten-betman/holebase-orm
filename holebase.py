# coding: utf-8
from sqlalchemy import BigInteger, CHAR, Column, DECIMAL, DateTime, Float, Index, Integer, LargeBinary, Table, Unicode, text
from sqlalchemy.dialects.mssql import BIT, DATETIME2, SMALLDATETIME, TINYINT, UNIQUEIDENTIFIER
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CORAggregateAbrasion(Base):
    __tablename__ = 'COR_AggregateAbrasion'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AggregateAbrasionValue = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORAggregateCrushingValue(Base):
    __tablename__ = 'COR_AggregateCrushingValue'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AggregateCrushingValue = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SizeFraction = Column(Unicode(255))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORAggregateElongationIndex(Base):
    __tablename__ = 'COR_AggregateElongationIndex'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AggregateElongationIndex = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORAggregateFlakines(Base):
    __tablename__ = 'COR_AggregateFlakiness'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AggregateFlakinessIndex = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Mass = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORAggregateImpactValue(Base):
    __tablename__ = 'COR_AggregateImpactValue'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AggregateImpactValueTest1 = Column(DECIMAL(19, 10))
    AggregateImpactValueTest2 = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    MeanAggregateImpactValue = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    ParticleDensity = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SizeFraction = Column(Unicode(255))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORAggregatePolishedStone(Base):
    __tablename__ = 'COR_AggregatePolishedStone'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AggregatePolishedStoneValue = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORAggregateResistanceToWear(Base):
    __tablename__ = 'COR_AggregateResistanceToWear'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DateFirstRun = Column(DATETIME2)
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    MeanMicroDevalDry = Column(DECIMAL(19, 10))
    MeanMicroDevalWet = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    MicroDevalCoefficient1 = Column(DECIMAL(19, 10))
    MicroDevalCoefficient2 = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SizeFraction = Column(Unicode(255))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORAggregateSoundnes(Base):
    __tablename__ = 'COR_AggregateSoundness'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AggregateSoundnessTest = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SizeFraction = Column(Unicode(255))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORAggregateWaterAbsorption(Base):
    __tablename__ = 'COR_AggregateWaterAbsorption'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AggregateWaterAbsorption = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORAllophaneContent(Base):
    __tablename__ = 'COR_AllophaneContent'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(50))
    AllophaneContent = Column(Unicode(50))
    AssociatedFileReference = Column(Unicode(50))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(50))
    SpecimenReference = Column(Unicode(50), index=True)
    Status = Column(Unicode(50))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORAuthUser(Base):
    __tablename__ = 'COR_AuthUser'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    Username = Column(Unicode(255))
    Password = Column(Unicode(255))
    Title = Column(UNIQUEIDENTIFIER)
    FirstName = Column(Unicode(255))
    Surname = Column(Unicode(255))
    Email = Column(Unicode(255))
    LandlineNumber = Column(Unicode(255))
    MobileNumber = Column(Unicode(255))
    IsActive = Column(BIT)
    IsExternal = Column(BIT)
    ExpiryDate = Column(DateTime)
    IsSysAdmin = Column(BIT)
    GridRowsCount = Column(Integer)
    ShowEmptyTreeNodes = Column(BIT)
    ShowInUsePicklists = Column(BIT)
    ZoomLevel = Column(Integer)
    Latitude = Column(DECIMAL(19, 10))
    Longitude = Column(DECIMAL(19, 10))
    AtMisUsername = Column(Unicode(255))
    AtMisPassword = Column(Unicode(255))
    PLogUsername = Column(Unicode(255))
    PLogPassword = Column(Unicode(255))
    AuthGroup = Column(UNIQUEIDENTIFIER, index=True)
    Domain = Column(Unicode(255))
    WindowsAuthentication = Column(BIT)
    DomainUsername = Column(Unicode(255))
    WMSProviderBGSUsername = Column(Unicode(255))
    WMSProviderBGSPassword = Column(Unicode(255))


class CORBackfillDetail(Base):
    __tablename__ = 'COR_BackfillDetails'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DateEnd = Column(DATETIME2)
    DepthBase = Column(DECIMAL(9, 3))
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Description = Column(Unicode(4000))
    Remarks = Column(Unicode(4000))
    LegendCode = Column(UNIQUEIDENTIFIER, index=True)
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORCBRDatum(Base):
    __tablename__ = 'COR_CBRData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    BulkDensityInitial = Column(DECIMAL(19, 10))
    CBRBase = Column(DECIMAL(19, 10))
    CBRTop = Column(DECIMAL(19, 10))
    DryDensityInitial = Column(DECIMAL(19, 10))
    MoistureContentBase = Column(DECIMAL(19, 10))
    MoistureContentInitial = Column(DECIMAL(19, 10))
    MoistureContentTop = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SoakingDetails = Column(Unicode(4000))
    SoakingSwelling = Column(DECIMAL(19, 10))
    SurchargePressure = Column(DECIMAL(19, 10))
    TestNumber = Column(Unicode(255), index=True)
    CBRGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORCBRGeneral(Base):
    __tablename__ = 'COR_CBRGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContentNatural = Column(DECIMAL(19, 10))
    PercentagePassing = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SieveSize = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    StabiliserAmount = Column(DECIMAL(19, 10))
    StabiliserType = Column(Unicode(255))
    Status = Column(Unicode(255))
    Swell = Column(DECIMAL(19, 10))
    SampleCondition = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORCasing(Base):
    __tablename__ = 'COR_Casing'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10), index=True)
    Remarks = Column(Unicode(4000))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORChainOfCustody(Base):
    __tablename__ = 'COR_ChainOfCustody'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    BatchReference = Column(Unicode(255))
    COCReference = Column(Unicode(255), index=True)
    DateDispatched = Column(DATETIME2)
    NumberofContainers = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SamplesFrom = Column(Unicode(255))
    SamplesTo = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORChalkCrushingValue(Base):
    __tablename__ = 'COR_ChalkCrushingValue'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    ChalkCrushingValue = Column(DECIMAL(19, 10))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    PercentageLargerThan10mm = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    WaterContentSpecimen = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORChiselling(Base):
    __tablename__ = 'COR_Chiselling'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3))
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Duration = Column(BigInteger)
    Remarks = Column(Unicode(4000))
    TimeStart = Column(DATETIME2)
    Tool = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORCompactionDatum(Base):
    __tablename__ = 'COR_CompactionData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    CompactionPointNumber = Column(Unicode(255), index=True)
    MaxDryDensity = Column(DECIMAL(19, 10))
    MoistureContent = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    CompactionGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORCompactionGeneral(Base):
    __tablename__ = 'COR_CompactionGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DryDensityMax = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContentOptimum = Column(DECIMAL(19, 10))
    ParticleDensity = Column(DECIMAL(19, 10))
    PercentagePassing1 = Column(DECIMAL(19, 10))
    PercentagePassing2 = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SieveSize1 = Column(DECIMAL(19, 10))
    SieveSize2 = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    StabiliserAmount = Column(DECIMAL(19, 10))
    StabiliserType = Column(Unicode(255))
    Status = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    MouldType = Column(UNIQUEIDENTIFIER, index=True)
    ParticleDensityMethod = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORConsolidationDatum(Base):
    __tablename__ = 'COR_ConsolidationData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    CoefficientofconsolidationLogTime = Column(DECIMAL(19, 10))
    CoefficientofconsolidationRootTime = Column(DECIMAL(19, 10))
    IncrementNumber = Column(Unicode(255), index=True)
    Remarks = Column(Unicode(4000))
    ReportedCoefficientOfConsolidation = Column(DECIMAL(19, 10))
    SecondaryCompressionCoefficient = Column(DECIMAL(19, 10))
    StressEnd = Column(DECIMAL(19, 10))
    TemperatureAverage = Column(DECIMAL(19, 10))
    VoidsRatioEnd = Column(DECIMAL(19, 10))
    VoidsRatioStart = Column(DECIMAL(19, 10))
    VolumeCompressibilityCoefficient = Column(DECIMAL(19, 10))
    ConsolidationGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORConsolidationGeneral(Base):
    __tablename__ = 'COR_ConsolidationGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BulkDensityInitial = Column(DECIMAL(19, 10))
    DefinedStressRange = Column(Unicode(255))
    DegreeOfSaturationInitial = Column(DECIMAL(19, 10))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    DryDensityInitial = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContentFinal = Column(DECIMAL(19, 10))
    MoistureContentInitial = Column(DECIMAL(19, 10))
    ParticleDensity = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SaturationHeightChange = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenHeight = Column(DECIMAL(19, 10))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SwellingPressure = Column(DECIMAL(19, 10))
    ParticleDensityMethod = Column(UNIQUEIDENTIFIER, index=True)
    SampleCondition = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    VoidsRatioInitial = Column(DECIMAL(19, 10))
    VolumeCompressibilityCoefficient = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORContaminant(Base):
    __tablename__ = 'COR_Contaminants'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BatchCode = Column(Unicode(255))
    ChemicalName = Column(Unicode(255))
    DateReceived = Column(DATETIME2)
    DateTimeLeachatePreparation = Column(DATETIME2)
    DateTimeTest = Column(DATETIME2)
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DilutionFactor = Column(DECIMAL(19, 10))
    InstrumentReference = Column(Unicode(255))
    InterpretedQualifiers = Column(Unicode(255))
    IsDetectFlag = Column(BIT)
    IsOrganic = Column(BIT)
    IsReportableResult = Column(BIT)
    LaboratoryName = Column(Unicode(255))
    LaboratoryQualifiers = Column(Unicode(255))
    LaboratoryTestName = Column(Unicode(255))
    LeachatePreparationMethod = Column(Unicode(255))
    MaterialSizeRemoved = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255), index=True)
    MethodDetectionLimit = Column(DECIMAL(19, 10))
    PercentageRemoved = Column(DECIMAL(19, 10))
    QuantificationLimit = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    ReportedResult = Column(Unicode(255))
    ReportingDetectionLimit = Column(DECIMAL(19, 10))
    ResultValue = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    TestName = Column(Unicode(255))
    TestNumber = Column(Unicode(255))
    TICProbability = Column(DECIMAL(19, 10))
    TICRetentionTime = Column(DECIMAL(19, 10))
    TotalOrDissolved = Column(Unicode(255))
    AnalysisLocation = Column(UNIQUEIDENTIFIER, index=True)
    Basis = Column(UNIQUEIDENTIFIER, index=True)
    ChemicalCode = Column(UNIQUEIDENTIFIER, index=True)
    Determinand = Column(UNIQUEIDENTIFIER, index=True)
    LaboratoryTestMatrix = Column(UNIQUEIDENTIFIER, index=True)
    ResultType = Column(UNIQUEIDENTIFIER, index=True)
    ResultUnit = Column(UNIQUEIDENTIFIER, index=True)
    RunType = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    UnitOfDetection = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORCoring(Base):
    __tablename__ = 'COR_Coring'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    Duration = Column(BigInteger)
    Remarks = Column(Unicode(4000))
    RQD = Column(DECIMAL(19, 10))
    SCR = Column(DECIMAL(19, 10))
    TCR = Column(DECIMAL(19, 10))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORDensity(Base):
    __tablename__ = 'COR_Density'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BulkDensity = Column(DECIMAL(19, 10))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DryDensity = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContent = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleCondition = Column(UNIQUEIDENTIFIER, index=True)
    SampleType = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORDepthRelatedExploratoryInformation(Base):
    __tablename__ = 'COR_DepthRelatedExploratoryInformation'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    BarrelLength = Column(DECIMAL(19, 10))
    BarrelType = Column(Unicode(255))
    BitCondition = Column(Unicode(255))
    DateLogged = Column(DATETIME2)
    DateTimeEnd = Column(DATETIME2)
    DateTimeStart = Column(DATETIME2)
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    DrillBitUsed = Column(Unicode(255))
    DrillingContractor = Column(Unicode(255))
    Logger = Column(Unicode(255))
    Method = Column(Unicode(255))
    PitLength = Column(DECIMAL(19, 10))
    PitStability = Column(Unicode(255))
    PitWidth = Column(DECIMAL(19, 10))
    PlantUsed = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    RigCrew = Column(Unicode(255))
    ShoringUsed = Column(Unicode(255))
    Type = Column(UNIQUEIDENTIFIER, index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORDepthRelatedRemark(Base):
    __tablename__ = 'COR_DepthRelatedRemarks'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Remarks = Column(Unicode(4000))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORDiscontinuity(Base):
    __tablename__ = 'COR_Discontinuities'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    ApertureMeasurement = Column(DECIMAL(19, 10))
    ApertureObservation = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Dip = Column(DECIMAL(19, 10))
    DipDirection = Column(DECIMAL(19, 10))
    DiscontinuityReference = Column(Unicode(255), index=True)
    DiscontinuitySetReference = Column(Unicode(255), index=True)
    InfillingMaterial = Column(Unicode(255))
    JointRoughnessCoefficient = Column(DECIMAL(19, 10))
    LargeScaleRoughnessAmplitude = Column(DECIMAL(19, 10))
    LargeScaleRoughnessWavelength = Column(DECIMAL(19, 10))
    MediumScaleRoughness = Column(Unicode(255))
    PersistenceMeasurement = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SeepageRating = Column(Unicode(255))
    SmallScaleRoughness = Column(Unicode(255))
    SurfaceAppearance = Column(Unicode(255))
    DiscontinuityType = Column(UNIQUEIDENTIFIER, index=True)
    Termination = Column(UNIQUEIDENTIFIER, index=True)
    WallStrength = Column(DECIMAL(19, 10))
    WallWeathering = Column(Unicode(255))
    WaterFlowEstimate = Column(DECIMAL(19, 10))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORDrillingFlush(Base):
    __tablename__ = 'COR_DrillingFlush'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    FlushColour = Column(Unicode(255))
    FlushReturnMaxPercentage = Column(DECIMAL(19, 10))
    FlushReturnMinPercentage = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    FlushType = Column(UNIQUEIDENTIFIER, index=True)
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORDrillingParameter(Base):
    __tablename__ = 'COR_DrillingParameters'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DateTimeBase = Column(DATETIME2)
    DateTimeTop = Column(DATETIME2)
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    DrillHeadRotationalSpeed = Column(DECIMAL(19, 10))
    DrillHeadRotationalTorque = Column(DECIMAL(19, 10))
    Duration = Column(BigInteger)
    FlushCirculation = Column(DECIMAL(19, 10))
    FlushPressure = Column(DECIMAL(19, 10))
    FlushRecovery = Column(DECIMAL(19, 10))
    HammeringUsed = Column(BIT)
    HoldbackForce = Column(DECIMAL(19, 10))
    HoldbackPressure = Column(DECIMAL(19, 10))
    PenetrationRate = Column(DECIMAL(19, 10))
    Pressure = Column(DECIMAL(19, 10))
    ReadingsReference = Column(Unicode(255), index=True)
    Remarks = Column(Unicode(4000))
    SpecificEnergy = Column(DECIMAL(19, 10))
    SupplyPressure = Column(DECIMAL(19, 10))
    Thrust = Column(DECIMAL(19, 10))
    Torque = Column(DECIMAL(19, 10))
    TorquePressure = Column(DECIMAL(19, 10))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORDynamic(Base):
    __tablename__ = 'COR_Dynamic'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DynamicElasticModulus = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    PWaveVelocity = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    ShearModulus = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SWaveVelocity = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORDynamicConePenetrometerDatum(Base):
    __tablename__ = 'COR_DynamicConePenetrometerData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    CumulativeBlows = Column(DECIMAL(19, 10), index=True)
    Delay = Column(BigInteger)
    Penetration = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    DynamicConePenetrometerGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORDynamicConePenetrometerGeneral(Base):
    __tablename__ = 'COR_DynamicConePenetrometerGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DateTest = Column(DATETIME2, index=True)
    DepthStart = Column(DECIMAL(9, 3), index=True)
    LayerRemarks = Column(Unicode(4000))
    Method = Column(Unicode(255))
    OrganisationName = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    Status = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    Weather = Column(Unicode(255))
    ZeroReading = Column(DECIMAL(19, 10))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORDynamicProbeDatum(Base):
    __tablename__ = 'COR_DynamicProbeData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    BlowsCumulative = Column(DECIMAL(19, 10))
    BlowsIncrement = Column(DECIMAL(19, 10))
    Delay = Column(BigInteger)
    DepthIncrement = Column(DECIMAL(9, 3))
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Remarks = Column(Unicode(4000))
    Torque = Column(DECIMAL(19, 10))
    DynamicProbeGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORDynamicProbeGeneral(Base):
    __tablename__ = 'COR_DynamicProbeGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AbortReason = Column(Unicode(255))
    AccreditionReference = Column(Unicode(255))
    AnvilDampertype = Column(Unicode(255))
    AnvilType = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BlowCountFrequency = Column(Unicode(255))
    ConeAngle = Column(DECIMAL(19, 10))
    DateTest = Column(DATETIME2)
    DiameterCone = Column(DECIMAL(19, 10))
    FinalConeDepth = Column(DECIMAL(9, 3))
    GroundwaterLevel = Column(DECIMAL(19, 10))
    HammerMass = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    OrganisationName = Column(Unicode(255))
    PreDrilling = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    RodDiameter = Column(DECIMAL(19, 10))
    RodFrictionPrecautions = Column(Unicode(255))
    RodMass = Column(DECIMAL(19, 10))
    StandardDrop = Column(DECIMAL(19, 10))
    Status = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    ProbeType = Column(UNIQUEIDENTIFIER, index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class COREffectiveStressConsolidationDatum(Base):
    __tablename__ = 'COR_EffectiveStressConsolidationData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    BackPressure = Column(DECIMAL(19, 10))
    CellPressure = Column(DECIMAL(19, 10))
    CoefficientOfConsolidation = Column(DECIMAL(19, 10))
    Coefficientofsecondarycompression = Column(DECIMAL(19, 10))
    CoefficientOfVolumeCompressibility = Column(DECIMAL(19, 10))
    ConsolidationSettlement = Column(DECIMAL(19, 10))
    ConsolidationVolumeChange = Column(DECIMAL(19, 10))
    CvMethod = Column(Unicode(255))
    EffectiveStressConsolidationEnd = Column(DECIMAL(19, 10))
    PercentagePorePressureDissipationEnd = Column(DECIMAL(19, 10))
    PorePressureConsolidationStageEnd = Column(DECIMAL(19, 10))
    PorePressureUndrainedLoadingEnd = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    StageNumber = Column(Unicode(255), index=True)
    Temperature = Column(DECIMAL(19, 10))
    VoidsRatioEnd = Column(DECIMAL(19, 10))
    VoidsRatioStart = Column(DECIMAL(19, 10))
    EffectiveStressConsolidationGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class COREffectiveStressConsolidationGeneral(Base):
    __tablename__ = 'COR_EffectiveStressConsolidationGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BackPressureSaturationEnd = Column(DECIMAL(19, 10))
    BulkDensityFinal = Column(DECIMAL(19, 10))
    BulkDensityInitial = Column(DECIMAL(19, 10))
    BValueSaturationEnd = Column(DECIMAL(19, 10))
    CellPressureSaturationEnd = Column(DECIMAL(19, 10))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    DifferentialPressure = Column(DECIMAL(19, 10))
    DrainageType = Column(Unicode(255))
    DryDensityInitial = Column(DECIMAL(19, 10))
    EquipmentType = Column(Unicode(255))
    InitialDegreeOfSaturation = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    LoadType = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContentFinal = Column(DECIMAL(19, 10))
    MoistureContentInitial = Column(DECIMAL(19, 10))
    ParticleDensity = Column(DECIMAL(19, 10))
    PorePressureLocation = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SaturationIncrements = Column(DECIMAL(19, 10))
    SaturationMethod = Column(Unicode(255))
    SaturationWaterVolume = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenHeight = Column(DECIMAL(19, 10))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SwellingPressure = Column(DECIMAL(19, 10))
    ParticleDensityMethod = Column(UNIQUEIDENTIFIER, index=True)
    SampleCondition = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    VoidsRatioInitial = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class COREnvironmentalContainerDetail(Base):
    __tablename__ = 'COR_EnvironmentalContainerDetails'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    ContainerID = Column(Unicode(4000))
    Remarks = Column(Unicode(4000))


class CORFlatDilatometerDatum(Base):
    __tablename__ = 'COR_FlatDilatometerData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(50))
    MinutesElapsed = Column(DECIMAL(19, 10), index=True)
    Reading = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    FlatDilatometerGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORFlatDilatometerGeneral(Base):
    __tablename__ = 'COR_FlatDilatometerGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(50))
    ChHorizontal = Column(DECIMAL(19, 10))
    DateTest = Column(DATETIME2)
    DepthTest = Column(DECIMAL(9, 3), index=True)
    kHorizontal = Column(DECIMAL(28, 19))
    Remarks = Column(Unicode(4000))
    tflexTime = Column(DECIMAL(19, 10))
    FlatDilatometerSeismicGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORFlatDilatometerSeismicDatum(Base):
    __tablename__ = 'COR_FlatDilatometerSeismicData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    APressure = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(50))
    BPressure = Column(DECIMAL(19, 10))
    BulkWeightEstimate = Column(DECIMAL(19, 10))
    CorrectedA = Column(DECIMAL(19, 10))
    CorrectedB = Column(DECIMAL(19, 10))
    CorrectedC = Column(DECIMAL(19, 10))
    CPressure = Column(DECIMAL(19, 10))
    DepthTest = Column(DECIMAL(9, 3), index=True)
    EffectiveVerticalStressEstimated = Column(DECIMAL(19, 10))
    PorewaterPressureEstimated = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    ShearWaveVelocity = Column(DECIMAL(19, 10))
    Thrust = Column(DECIMAL(19, 10))
    TotalVerticalStressEstimated = Column(DECIMAL(19, 10))
    EstimationMethod = Column(UNIQUEIDENTIFIER, index=True)
    FlatDilatometerSeismicGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORFlatDilatometerSeismicDerived(Base):
    __tablename__ = 'COR_FlatDilatometerSeismicDerived'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(50))
    Cu = Column(DECIMAL(19, 10))
    Dilatometermodulus = Column(DECIMAL(19, 10))
    G0 = Column(DECIMAL(19, 10))
    Horizontalsressindex = Column(DECIMAL(19, 10))
    InternalFriction = Column(DECIMAL(19, 10))
    InterpretationReference = Column(Unicode(50), index=True)
    Interpretedsoildescription = Column(Unicode(4000))
    K0 = Column(DECIMAL(19, 10))
    M = Column(DECIMAL(19, 10))
    Materialindex = Column(DECIMAL(19, 10))
    OCR = Column(DECIMAL(19, 10))
    qD = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    FlatDilatometerSeismicData = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORFlatDilatometerSeismicGeneral(Base):
    __tablename__ = 'COR_FlatDilatometerSeismicGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(50))
    BladeCalibrationA = Column(DECIMAL(19, 10))
    BladeCalibrationB = Column(DECIMAL(19, 10))
    BladeNumber = Column(Unicode(50))
    CorrectionFactor = Column(Unicode(50))
    DateTest = Column(DATETIME2)
    DepthGroundwater = Column(DECIMAL(9, 3))
    Operators = Column(Unicode(50))
    ReactionMethod = Column(Unicode(50))
    Remarks = Column(Unicode(4000))
    RigType = Column(Unicode(50))
    RodType = Column(Unicode(50))
    SeismicNumber = Column(Unicode(50))
    Standard = Column(Unicode(50))
    Subcontractor = Column(Unicode(50))
    TestNumber = Column(Unicode(50), index=True)
    ThrustMeasurementMethod = Column(Unicode(50))
    GroundwaterMethod = Column(UNIQUEIDENTIFIER, index=True)
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORFractureSpacing(Base):
    __tablename__ = 'COR_FractureSpacing'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    DiscontinuityReference = Column(Unicode(255), index=True)
    FI = Column(Unicode(255))
    FIValue = Column(DECIMAL(19, 10))
    FractureSpacingAverage = Column(DECIMAL(19, 10))
    FractureSpacingMax = Column(DECIMAL(19, 10))
    FractureSpacingMin = Column(Unicode(255))
    FractureSpacingMinValue = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORFrostSusceptibility(Base):
    __tablename__ = 'COR_FrostSusceptibility'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DryDensity = Column(DECIMAL(19, 10))
    Heave1 = Column(DECIMAL(19, 10))
    Heave2 = Column(DECIMAL(19, 10))
    Heave3 = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    MeanHeave = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    PreparationMoistureContent = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    StabiliserAmount = Column(DECIMAL(19, 10))
    StabiliserType = Column(Unicode(255))
    Status = Column(Unicode(255))
    SampleCondition = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORGeotechnicalChemistry(Base):
    __tablename__ = 'COR_GeotechnicalChemistry'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DeterminandName = Column(Unicode(255))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255), index=True)
    Remarks = Column(Unicode(4000))
    ReportedResult = Column(Unicode(255))
    Result = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    Determinand = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    Unit = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORHistoricProject(Base):
    __tablename__ = 'COR_HistoricProject'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ClientName = Column(Unicode(255))
    ContractorName = Column(Unicode(255))
    Engineer = Column(Unicode(255))
    Location = Column(Unicode(255))
    Memo = Column(Unicode(255))
    Reference = Column(Unicode(255))
    Title = Column(Unicode(255))


class CORHoleDiameter(Base):
    __tablename__ = 'COR_HoleDiameters'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10), index=True)
    Remarks = Column(Unicode(4000))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORInSituCBR(Base):
    __tablename__ = 'COR_InSituCBR'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    CBRValue = Column(DECIMAL(19, 10))
    DateTest = Column(DATETIME2)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Kentledge = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContent = Column(DECIMAL(19, 10))
    OrganisationName = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SeatingForce = Column(DECIMAL(19, 10))
    Status = Column(Unicode(255))
    StratumReference = Column(Unicode(255))
    SurchargePressure = Column(DECIMAL(19, 10))
    TestNumber = Column(Unicode(255), index=True)
    CBRType = Column(UNIQUEIDENTIFIER, index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORInSituDensity(Base):
    __tablename__ = 'COR_InSituDensity'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BulkDensityInSitu = Column(DECIMAL(19, 10))
    DateTest = Column(DATETIME2)
    Depth = Column(DECIMAL(9, 3), index=True)
    Method = Column(Unicode(255))
    MoistureContent = Column(DECIMAL(19, 10))
    OrganisationName = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    StabiliserAmount = Column(DECIMAL(19, 10))
    StabiliserType = Column(Unicode(255))
    Status = Column(Unicode(255))
    StratumReference = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORInSituHandPenetrometer(Base):
    __tablename__ = 'COR_InSituHandPenetrometer'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DateTest = Column(DATETIME2)
    Depth = Column(DECIMAL(9, 3), index=True)
    HandPenetrometer = Column(Unicode(255))
    HandPenetrometerValue = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    OrganisationName = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    Status = Column(Unicode(255))
    StratumReference = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORInSituPermeabilityDatum(Base):
    __tablename__ = 'COR_InSituPermeabilityData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthWater = Column(Unicode(50))
    Remarks = Column(Unicode(4000))
    TimeElapsed = Column(BigInteger, index=True)
    InSituPermeabilityGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORInSituPermeabilityGeneral(Base):
    __tablename__ = 'COR_InSituPermeabilityGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AppliedHeadOfWater = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    AverageFlow = Column(DECIMAL(19, 10))
    DateTest = Column(DATETIME2)
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthStandingWater = Column(DECIMAL(9, 3))
    DepthTop = Column(DECIMAL(9, 3), index=True)
    DepthWaterBeforeTest = Column(Unicode(50))
    DepthWaterStart = Column(Unicode(50))
    DiameterCasing = Column(DECIMAL(19, 10))
    DiameterTestZone = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    OrganisationName = Column(Unicode(255))
    Permeability = Column(DECIMAL(28, 19))
    Remarks = Column(Unicode(4000))
    StageNumber = Column(DECIMAL(19, 10), index=True)
    Status = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORInSituRedox(Base):
    __tablename__ = 'COR_InSituRedox'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DateTest = Column(DATETIME2)
    Depth = Column(DECIMAL(9, 3), index=True)
    MeanPotential = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    OrganisationName = Column(Unicode(255))
    Ph = Column(DECIMAL(19, 10))
    RedoxPotential = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    Status = Column(Unicode(255))
    StratumReference = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORInSituResistivity(Base):
    __tablename__ = 'COR_InSituResistivity'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    ApparentResistivity1 = Column(DECIMAL(19, 10))
    ApparentResistivity2 = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    DateTest = Column(DATETIME2)
    Depth = Column(DECIMAL(9, 3), index=True)
    DepthBase = Column(DECIMAL(9, 3))
    MeanSwellingPressure = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    OrganisationName = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    Status = Column(Unicode(255))
    StratumReference = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORInSituVane(Base):
    __tablename__ = 'COR_InSituVane'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DateTest = Column(DATETIME2)
    Depth = Column(DECIMAL(9, 3), index=True)
    Method = Column(Unicode(255))
    OrganisationName = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    Residualresult = Column(Unicode(255))
    ResidualresultValue = Column(DECIMAL(19, 10))
    Result = Column(Unicode(255))
    ResultValue = Column(DECIMAL(19, 10))
    Status = Column(Unicode(255))
    StratumReference = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    VaneType = Column(UNIQUEIDENTIFIER, index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORInitialConsumptionOfLimeDatum(Base):
    __tablename__ = 'COR_InitialConsumptionOfLimeData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    LimepH = Column(DECIMAL(19, 10))
    PercentageLime = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    TestNumber = Column(Unicode(255), index=True)
    InitialConsumptionOfLimeGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORInitialConsumptionOfLimeGeneral(Base):
    __tablename__ = 'COR_InitialConsumptionOfLimeGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    InitialLimeConsumption = Column(DECIMAL(19, 10))
    InterpretationpH = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    LimeDetails = Column(Unicode(4000))
    Method = Column(Unicode(255))
    PercentagePassing = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SaturatedLimeSolutionpH = Column(DECIMAL(19, 10))
    SizePassing = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORLaboratory(Base):
    __tablename__ = 'COR_Laboratory'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    LaboratoryName = Column(Unicode(255), index=True)
    Address = Column(Unicode(255))
    Telephone = Column(Unicode(255))
    Email = Column(Unicode(255))
    LabManagerName = Column(Unicode(255))
    Accreditation = Column(Unicode(255))


class CORLaboratoryHandPenetrometer(Base):
    __tablename__ = 'COR_LaboratoryHandPenetrometer'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContent = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    UndrainedShearStrength = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORLaboratoryPermeability(Base):
    __tablename__ = 'COR_LaboratoryPermeability'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BulkDensityInitial = Column(DECIMAL(19, 10))
    CoefficientOfPermeability = Column(DECIMAL(28, 19))
    ConsolidationDetails = Column(Unicode(4000))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DiameterDrain = Column(DECIMAL(19, 10))
    DiameterSpecimen = Column(DECIMAL(19, 10))
    DrainMethod = Column(Unicode(255))
    DryDensityInitial = Column(DECIMAL(19, 10))
    HydraulicGradient = Column(DECIMAL(19, 10))
    InitialDegreeOfSaturation = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    MaterialRemoved = Column(DECIMAL(19, 10))
    MeanEffectiveStress = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    MoistureContentInitial = Column(DECIMAL(19, 10))
    ParticleDensity = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SaturationDetails = Column(Unicode(4000))
    SizeCutOff = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenLength = Column(DECIMAL(19, 10))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    ParticleDensityMethod = Column(UNIQUEIDENTIFIER, index=True)
    PermeameterType = Column(UNIQUEIDENTIFIER, index=True)
    SampleCondition = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    VoidsRatioInitial = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORLaboratoryResistivity(Base):
    __tablename__ = 'COR_LaboratoryResistivity'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BulkDensity = Column(DECIMAL(19, 10))
    ContainerArea = Column(DECIMAL(19, 10))
    ContainerLength = Column(DECIMAL(19, 10))
    ContainerShape = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    DryDensity = Column(DECIMAL(19, 10))
    ElectrodesType = Column(Unicode(255))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContent = Column(DECIMAL(19, 10))
    PercentageRemoved = Column(Unicode(255))
    Probedetails = Column(Unicode(4000))
    Remarks = Column(Unicode(4000))
    ResistivityTemperatureCorrected = Column(DECIMAL(19, 10))
    SampleCondition = Column(Unicode(255))
    SaturationWaterVolume = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    Temperature = Column(DECIMAL(19, 10))
    WaterResitivity = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORLaboratoryVane(Base):
    __tablename__ = 'COR_LaboratoryVane'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    EquivalentDiameter = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContent = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    UndrainedShearStrengthPeak = Column(DECIMAL(19, 10))
    UndrainedShearStrengthRemolded = Column(DECIMAL(19, 10))
    VaneType = Column(UNIQUEIDENTIFIER, index=True)
    VaneLength = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORLinearShrinkage(Base):
    __tablename__ = 'COR_LinearShrinkage'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    LinearShrinkage = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    PercentagePassing = Column(DECIMAL(19, 10))
    Preparation = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SizePassing = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORLiquidAndPlasticLimit(Base):
    __tablename__ = 'COR_LiquidAndPlasticLimit'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    LiquidLimit = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    PercentagePassing = Column(DECIMAL(19, 10))
    PlasticityIndex = Column(DECIMAL(19, 10))
    PlasticLimit = Column(Unicode(255))
    PlasticLimitValue = Column(DECIMAL(19, 10))
    Preparation = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SizePassing = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    StabiliserAmount = Column(DECIMAL(19, 10))
    StabiliserType = Column(Unicode(255))
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORLocationDetail(Base):
    __tablename__ = 'COR_LocationDetails'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AlignmentID = Column(Unicode(255))
    ApprovedBy = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    Chainage = Column(Unicode(255))
    CheckedBy = Column(Unicode(255))
    DateEnd = Column(DATETIME2)
    DateStart = Column(DATETIME2)
    Easting = Column(DECIMAL(19, 10))
    EastingTraverseEnd = Column(DECIMAL(19, 10))
    FinalDepth = Column(DECIMAL(9, 3))
    GridLetterReference = Column(Unicode(255))
    GroundLevel = Column(DECIMAL(19, 10))
    GroundLevelEnd = Column(DECIMAL(19, 10))
    Latitude = Column(Unicode(255))
    LatitudeEnd = Column(Unicode(255))
    LocalDatum = Column(Unicode(255))
    LocalGridSystem = Column(Unicode(255))
    LocalLevel = Column(DECIMAL(19, 10))
    LocalLevelEnd = Column(DECIMAL(19, 10))
    LocalXEnd = Column(DECIMAL(19, 10))
    LocalXGrid = Column(DECIMAL(19, 10))
    LocalYEnd = Column(DECIMAL(19, 10))
    LocalYGrid = Column(DECIMAL(19, 10))
    LocationID = Column(Unicode(255), index=True)
    LocationingMethod = Column(Unicode(255))
    LocationPurpose = Column(Unicode(255))
    Longitude = Column(Unicode(255))
    LongitudeEnd = Column(Unicode(255))
    Northing = Column(DECIMAL(19, 10))
    NorthingTraverseEnd = Column(DECIMAL(19, 10))
    Offset = Column(DECIMAL(19, 10))
    Phase = Column(Unicode(255))
    ProjectionFormat = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SubLocation = Column(Unicode(255))
    TerminationReason = Column(Unicode(255))
    Transformation = Column(Unicode(255))
    LocationType = Column(UNIQUEIDENTIFIER, index=True)
    NationalGridReferencingSystem = Column(UNIQUEIDENTIFIER, index=True)
    Status = Column(UNIQUEIDENTIFIER, index=True)
    Centroid = Column(NullType)
    LongLatCentroid = Column(NullType)
    BingCentroid = Column(NullType, index=True)
    GraphSeriesStyleDefinition = Column(UNIQUEIDENTIFIER, index=True)
    LatitudeNumeric = Column(DECIMAL(19, 10))
    LongitudeNumeric = Column(DECIMAL(19, 10))
    OriginalId = Column(Unicode(255))
    HistoricProject = Column(UNIQUEIDENTIFIER, index=True)
    WellCapType = Column(UNIQUEIDENTIFIER)


class CORLocationGroup(Base):
    __tablename__ = 'COR_LocationGroup'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    GroupName = Column(Unicode(255))
    Bounds = Column(NullType)
    LongLatBounds = Column(NullType)
    BingBounds = Column(NullType, index=True)


class CORLocationGroupLink(Base):
    __tablename__ = 'COR_LocationGroupLink'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    LocationGroup = Column(UNIQUEIDENTIFIER, index=True)
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORLosAngelesAbrasion(Base):
    __tablename__ = 'COR_LosAngelesAbrasion'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    ChargeGrading = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    LosAngelesCoefficient = Column(DECIMAL(19, 10))
    LosAngelesPercentageWear = Column(DECIMAL(19, 10))
    LosAngelesWearRatio = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SizeFraction = Column(Unicode(255))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORMCVDatum(Base):
    __tablename__ = 'COR_MCVData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    BlowDifference = Column(DECIMAL(19, 10))
    BulkDensity = Column(DECIMAL(19, 10))
    interpretationMethod = Column(Unicode(255))
    MCV = Column(DECIMAL(19, 10))
    MoistureContent = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    StrengthAgainstStandard = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    MCVGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORMCVGeneral(Base):
    __tablename__ = 'COR_MCVGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    NaturalMoistureContent = Column(DECIMAL(19, 10))
    PercentagePassing = Column(DECIMAL(19, 10))
    PrecalibratedValue = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SieveSize = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    StabiliserAmount = Column(DECIMAL(19, 10))
    StabiliserType = Column(Unicode(255))
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORMoistureContent(Base):
    __tablename__ = 'COR_MoistureContent'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    AssumedReason = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DryingTemperature = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContent = Column(DECIMAL(19, 10))
    MoistureContentNatural = Column(BIT)
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    StabiliserAmount = Column(DECIMAL(19, 10))
    StabiliserType = Column(Unicode(255))
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORMonitoringInstallationPipeWork(Base):
    __tablename__ = 'COR_MonitoringInstallationPipeWork'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    PipeDetails = Column(Unicode(4000))
    PipeReference = Column(Unicode(255), index=True)
    Remarks = Column(Unicode(4000))
    PipeType = Column(UNIQUEIDENTIFIER, index=True)
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORMonitoringInstallationsAndInstrument(Base):
    __tablename__ = 'COR_MonitoringInstallationsAndInstruments'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    BearingA = Column(DECIMAL(19, 10))
    BearingB = Column(DECIMAL(19, 10))
    BearingC = Column(DECIMAL(19, 10))
    Contractor = Column(Unicode(255))
    DateInstallation = Column(DATETIME2)
    DepthResponseZoneBase = Column(DECIMAL(9, 3))
    DepthResponseZoneTop = Column(DECIMAL(9, 3))
    Distance = Column(DECIMAL(19, 10), index=True)
    InclinationA = Column(DECIMAL(19, 10))
    InclinationB = Column(DECIMAL(19, 10))
    InclinationC = Column(DECIMAL(19, 10))
    InstrumentDetails = Column(Unicode(4000))
    PipeReference = Column(Unicode(255))
    PointReference = Column(Unicode(255), index=True)
    Remarks = Column(Unicode(4000))
    SignConventionA = Column(Unicode(255))
    SignConventionB = Column(Unicode(255))
    SignConventionC = Column(Unicode(255))
    InstrumentType = Column(UNIQUEIDENTIFIER, index=True)
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    PipeElevation = Column(DECIMAL(19, 10))
    PipeHeight = Column(DECIMAL(19, 10))
    PipeCoverType = Column(UNIQUEIDENTIFIER)


class CORMonitoringReading(Base):
    __tablename__ = 'COR_MonitoringReadings'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DateTime = Column(DATETIME2, index=True)
    InstrumentDetectionLimit = Column(DECIMAL(19, 10))
    InstrumentReference = Column(Unicode(255))
    InstrumentUpperLimit = Column(DECIMAL(19, 10))
    MeasurementName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Organisation = Column(Unicode(255))
    Reading = Column(DECIMAL(19, 10))
    ReadingReference = Column(Unicode(255), index=True)
    ReadingText = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    ReadingType = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    Unit = Column(UNIQUEIDENTIFIER, index=True)
    MonitoringInstallationsAndInstruments = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class COROffice(Base):
    __tablename__ = 'COR_Office'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    Name = Column(Unicode(255))
    OfficeAddress = Column(Unicode(4000))
    PostalAddress = Column(Unicode(4000))
    Region = Column(UNIQUEIDENTIFIER)
    Country = Column(UNIQUEIDENTIFIER)
    Telephone = Column(Unicode(255))
    Fax = Column(Unicode(255))
    Email = Column(Unicode(255))
    Website = Column(Unicode(255))
    Manager = Column(Unicode(255))
    Logo = Column(LargeBinary)


class COROnSiteFID(Base):
    __tablename__ = 'COR_OnSiteFID'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DateTest = Column(DATETIME2)
    Depth = Column(DECIMAL(9, 3), index=True)
    FIDResult = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    OrganisationName = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    Status = Column(Unicode(255))
    StratumReference = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class COROnSitePID(Base):
    __tablename__ = 'COR_OnSitePID'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DateTest = Column(DATETIME2)
    Depth = Column(DECIMAL(9, 3), index=True)
    Method = Column(Unicode(255))
    OrganisationName = Column(Unicode(255))
    PIDResult = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    Status = Column(Unicode(255))
    StratumReference = Column(Unicode(255))
    Temperature = Column(DECIMAL(19, 10))
    TestNumber = Column(Unicode(255), index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class COROrganicContent(Base):
    __tablename__ = 'COR_OrganicContent'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(50))
    AssociatedFileReference = Column(Unicode(50))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    OrganicContent = Column(Unicode(50))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(50))
    SpecimenReference = Column(Unicode(50), index=True)
    Status = Column(Unicode(50))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class COROrientationAndInclination(Base):
    __tablename__ = 'COR_OrientationAndInclination'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Inclination = Column(DECIMAL(19, 10))
    Orientation = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORParticleDensity(Base):
    __tablename__ = 'COR_ParticleDensity'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    ParticleDensity = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    ParticleDensityMethod = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORParticleSizeDistributionDatum(Base):
    __tablename__ = 'COR_ParticleSizeDistributionData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    ParticleSize = Column(DECIMAL(19, 10), index=True)
    PercentagePassing = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    ParticleSizeDistributionGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORParticleSizeDistributionGeneral(Base):
    __tablename__ = 'COR_ParticleSizeDistributionGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    PercentageClay = Column(DECIMAL(19, 10))
    PercentageCobbles = Column(DECIMAL(19, 10))
    PercentageFines = Column(DECIMAL(19, 10))
    PercentageGravel = Column(DECIMAL(19, 10))
    PercentageSand = Column(DECIMAL(19, 10))
    PercentageSilt = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    UniformityCoefficient = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORPinholeDispersion(Base):
    __tablename__ = 'COR_PinholeDispersion'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(50))
    AssociatedFileReference = Column(Unicode(50))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(50))
    SpecimenReference = Column(Unicode(50), index=True)
    Status = Column(Unicode(50))
    PinholeClass = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORPlateLoadingDatum(Base):
    __tablename__ = 'COR_PlateLoadingData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AppliedLoad = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    LoadStage = Column(Unicode(255), index=True)
    Remarks = Column(Unicode(4000))
    SettlementGauge1 = Column(DECIMAL(19, 10))
    SettlementGauge2 = Column(DECIMAL(19, 10))
    SettlementGauge3 = Column(DECIMAL(19, 10))
    SettlementGauge4 = Column(DECIMAL(19, 10))
    StageElapsedTime = Column(DECIMAL(19, 10), index=True)
    PlateLoadingGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORPlateLoadingGeneral(Base):
    __tablename__ = 'COR_PlateLoadingGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DateTest = Column(DATETIME2)
    Depth = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    ElasticModulus = Column(DECIMAL(19, 10))
    ElasticModulus2 = Column(DECIMAL(19, 10))
    FactorA0 = Column(DECIMAL(19, 10))
    FactorA1 = Column(DECIMAL(19, 10))
    FactorA2 = Column(DECIMAL(19, 10))
    LoadCycle = Column(Unicode(255), index=True)
    Method = Column(Unicode(255))
    ModulusOfSubgradeReaction = Column(DECIMAL(19, 10))
    OrganisationName = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SeatingLoad = Column(DECIMAL(19, 10))
    StabiliserAmount = Column(DECIMAL(19, 10))
    StabiliserType = Column(Unicode(255))
    Status = Column(Unicode(255))
    Strainmodulus = Column(DECIMAL(19, 10))
    StratumReference = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORPointLoad(Base):
    __tablename__ = 'COR_PointLoads'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    PointLoadSizeCorrected = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    UncorrectedPointLoad = Column(DECIMAL(19, 10))
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    WaterContentSpecimen = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORPressuremeterDatum(Base):
    __tablename__ = 'COR_PressuremeterData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    Axis1Displacement = Column(DECIMAL(19, 10))
    Axis2Displacement = Column(DECIMAL(19, 10))
    Axis3Displacement = Column(DECIMAL(19, 10))
    PorePressureCellA = Column(DECIMAL(19, 10))
    PorePressureCellB = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SequenceNumber = Column(DECIMAL(19, 10), index=True)
    TotalPressure = Column(DECIMAL(19, 10))
    VolumeChange = Column(DECIMAL(19, 10))
    PressuremeterResultsGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    TotalPressure1 = Column(DECIMAL(19, 10))
    TotalPressure2 = Column(DECIMAL(12, 3))
    TotalPressure3 = Column(DECIMAL(19, 10))


class CORPressuremeterResultsGeneral(Base):
    __tablename__ = 'COR_PressuremeterResultsGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AngleOfDilation = Column(DECIMAL(19, 10))
    AngleOfFriction = Column(DECIMAL(19, 10))
    AngleOfFrictionAtConstantVolume = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(255))
    DateTest = Column(DATETIME2)
    Depth = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    InitialShearModulus = Column(DECIMAL(19, 10))
    InSituHorizontalStress = Column(DECIMAL(19, 10))
    InstrumentReference = Column(Unicode(255))
    LimitPressure = Column(DECIMAL(19, 10))
    MeasuredorAssumed = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    Operator = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    Status = Column(Unicode(255))
    SubContractor = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    UndrainedShearStrength = Column(DECIMAL(19, 10))
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    AngleOfDilation1 = Column(DECIMAL(12, 3))
    Measured_or_assumed_ground_water_level = Column('Measured or assumed ground water level', DECIMAL(12, 3))
    AngleOfDilation3 = Column(DECIMAL(12, 3))
    AngleOfFriction1 = Column(DECIMAL(12, 3))
    AngleOfFriction2 = Column(DECIMAL(12, 3))
    AngleOfFriction3 = Column(DECIMAL(12, 3))
    AngleOfDilation2 = Column(DECIMAL(12, 3))
    InitialShearModulus1 = Column(DECIMAL(19, 10))
    InitialShearModulus2 = Column(DECIMAL(19, 10))
    InitialShearModulus3 = Column(DECIMAL(19, 10))
    HorizontalStress1 = Column(DECIMAL(19, 10))
    HorizontalStress2 = Column(DECIMAL(19, 10))
    HorizontalStress3 = Column(DECIMAL(19, 10))
    LimitPressure1 = Column(DECIMAL(19, 10))
    LimitPressure2 = Column(DECIMAL(19, 10))
    LimitPressure3 = Column(DECIMAL(19, 10))
    UndrainedShearStrength1 = Column(DECIMAL(19, 10))
    UndrainedShearStrength2 = Column(DECIMAL(19, 10))
    UndrainedShearStrength3 = Column(DECIMAL(19, 10))


class CORPressuremeterResultsIndividualLoop(Base):
    __tablename__ = 'COR_PressuremeterResultsIndividualLoops'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    AverageShearModulus = Column(DECIMAL(19, 10))
    LinearityExponent = Column(DECIMAL(19, 10))
    LoopNumber = Column(DECIMAL(19, 10), index=True)
    MeanPressure = Column(DECIMAL(19, 10))
    MeanStrain = Column(DECIMAL(19, 10))
    PressureRange = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    ShearStressCoefficient = Column(DECIMAL(19, 10))
    StrainRange = Column(DECIMAL(19, 10))
    PressuremeterData = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ShearModulus2 = Column(DECIMAL(19, 10))
    ShearModulus3 = Column(DECIMAL(19, 10))
    ShearModulus1 = Column(DECIMAL(19, 10))


class CORProgressByTime(Base):
    __tablename__ = 'COR_ProgressByTime'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DateTime = Column(DATETIME2, index=True)
    Depth = Column(DECIMAL(9, 3))
    DepthCasing = Column(DECIMAL(9, 3))
    DepthWater = Column(Unicode(255))
    DepthWaterValue = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORProject(Base):
    __tablename__ = 'COR_Project'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(50))
    AutomaticallyCreateUndefinedPicklistEntries = Column(BIT)
    AutomaticallyImportAbbreviations = Column(BIT)
    ClientName = Column(Unicode(255))
    ContractorsName = Column(Unicode(255))
    HasData = Column(BIT)
    InitialLatitude = Column(DECIMAL(19, 10))
    InitialLongitude = Column(DECIMAL(19, 10))
    InitialZoomLevel = Column(Integer)
    IsCustomised = Column(BIT)
    Latitude = Column(DECIMAL(19, 10))
    Longitude = Column(DECIMAL(19, 10))
    ProjectEngineer = Column(Unicode(255))
    ProjectID = Column(Unicode(50), index=True)
    ProjectTitle = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    RequiresDbRebuild = Column(BIT)
    SiteLocation = Column(Unicode(255))
    Category = Column(UNIQUEIDENTIFIER, index=True)
    Status = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    MapCoordinateSystem = Column(UNIQUEIDENTIFIER, index=True)
    Bounds = Column(NullType)
    LongLatBounds = Column(NullType)
    BingBounds = Column(NullType, index=True)
    Centroid = Column(NullType)
    LongLatCentroid = Column(NullType)
    BingCentroid = Column(NullType, index=True)
    ExternalId = Column(Unicode(255))
    PLogLastUpdated = Column(DateTime)
    RequiresReCalculation = Column(BIT)
    PickListSetDefinition = Column(UNIQUEIDENTIFIER, index=True)
    Office = Column(UNIQUEIDENTIFIER, index=True)
    Logo = Column(LargeBinary)


class CORPumpingDatum(Base):
    __tablename__ = 'COR_PumpingData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DateTimeReading = Column(DATETIME2, index=True)
    Depth = Column(Unicode(50))
    PumpingRate = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    PumpingGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORPumpingGeneral(Base):
    __tablename__ = 'COR_PumpingGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    Contractor = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    Status = Column(Unicode(255))
    TestReference = Column(Unicode(255), index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORRelativeDensity(Base):
    __tablename__ = 'COR_RelativeDensity'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DryDensityMax = Column(DECIMAL(19, 10))
    DryDensityMin = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    PercentagePassing1 = Column(DECIMAL(19, 10))
    PercentagePassing2 = Column(DECIMAL(19, 10))
    PercentagePassing3 = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SieveSize1 = Column(DECIMAL(19, 10))
    SieveSize2 = Column(DECIMAL(19, 10))
    SieveSize3 = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORRingShearDatum(Base):
    __tablename__ = 'COR_RingShearData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AngularDisplacement = Column(DECIMAL(19, 10))
    AngularRate = Column(DECIMAL(19, 10))
    AssociatedFileReference = Column(Unicode(50))
    BulkDensityInitial = Column(DECIMAL(19, 10))
    DiameterInner = Column(DECIMAL(19, 10))
    DiameterOuter = Column(DECIMAL(19, 10))
    DryDensityInitial = Column(DECIMAL(19, 10))
    LinearDisplacement = Column(DECIMAL(19, 10))
    MoistureContentFinal = Column(DECIMAL(19, 10))
    MoistureContentInitial = Column(DECIMAL(19, 10))
    NormalStress = Column(DECIMAL(19, 10))
    ParticleDensity = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    ResidualShearStress = Column(DECIMAL(19, 10))
    ResidualStrengthCriterion = Column(Unicode(255))
    ResidualStressDisplacementRate = Column(DECIMAL(19, 10))
    SpecimenHeight = Column(DECIMAL(19, 10))
    StageNumber = Column(Unicode(50), index=True)
    ParticleDensityMethod = Column(UNIQUEIDENTIFIER, index=True)
    VoidsRatioInitial = Column(DECIMAL(19, 10))
    RingShearGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORRingShearGeneral(Base):
    __tablename__ = 'COR_RingShearGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(50))
    Condition = Column(Unicode(50))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    Residualcohesionintercept = Column(DECIMAL(19, 10))
    ResidualFrictionAngle = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(50))
    SpecimenReference = Column(Unicode(50), index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORRockPorosityAndDensity(Base):
    __tablename__ = 'COR_RockPorosityAndDensity'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BulkDensity = Column(DECIMAL(19, 10))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DryDensity = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    ParticleDensity = Column(DECIMAL(19, 10))
    Porosity = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    Temperature = Column(DECIMAL(19, 10))
    WaterContentSaturated = Column(DECIMAL(19, 10))
    WaterContentSpecimen = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORRockUniaxialCompressiveStrengthAndDeformability(Base):
    __tablename__ = 'COR_RockUniaxialCompressiveStrengthAndDeformability'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    FailureMode = Column(Unicode(255))
    LaboratoryName = Column(Unicode(255))
    Machinetype = Column(Unicode(255))
    Method = Column(Unicode(255))
    PoissonsRatio = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenCondition = Column(Unicode(255))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenLength = Column(DECIMAL(19, 10))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    StressLevel = Column(Unicode(255))
    StressRate = Column(DECIMAL(19, 10))
    TestDuration = Column(BigInteger)
    UniaxialCompressiveStrength = Column(DECIMAL(19, 10))
    YoungsModulusMethod = Column(UNIQUEIDENTIFIER, index=True)
    WaterContentSpecimen = Column(DECIMAL(19, 10))
    YoungsModulus = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORSPT(Base):
    __tablename__ = 'COR_SPT'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BlowsMain1 = Column(DECIMAL(19, 10))
    BlowsMain2 = Column(DECIMAL(19, 10))
    BlowsMain3 = Column(DECIMAL(19, 10))
    BlowsMain4 = Column(DECIMAL(19, 10))
    BlowsMainTotal = Column(DECIMAL(19, 10))
    BlowsSeating = Column(DECIMAL(19, 10))
    BlowsSeating1 = Column(DECIMAL(19, 10))
    BlowsSeating2 = Column(DECIMAL(19, 10))
    DepthCasing = Column(DECIMAL(9, 3))
    DepthTop = Column(DECIMAL(9, 3), index=True)
    DepthWater = Column(Unicode(255))
    DepthWaterValue = Column(DECIMAL(19, 10))
    EnergyRatio = Column(DECIMAL(19, 10))
    HammerSerialNumber = Column(Unicode(255))
    IsSoftRock = Column(BIT)
    Method = Column(Unicode(255))
    NValue = Column(DECIMAL(19, 10))
    PenetrationMain1 = Column(DECIMAL(19, 10))
    PenetrationMain2 = Column(DECIMAL(19, 10))
    PenetrationMain3 = Column(DECIMAL(19, 10))
    PenetrationMain4 = Column(DECIMAL(19, 10))
    PenetrationSeating1 = Column(DECIMAL(19, 10))
    PenetrationSeating2 = Column(DECIMAL(19, 10))
    PenetrationTotal = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    ReportedResult = Column(Unicode(255))
    SelfWeightPenetration = Column(DECIMAL(19, 10))
    Status = Column(Unicode(255))
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORSampleInformation(Base):
    __tablename__ = 'COR_SampleInformation'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    BarometricPressure = Column(DECIMAL(19, 10))
    Blows = Column(DECIMAL(19, 10))
    Caption = Column(Unicode(255))
    Classification = Column(Unicode(255))
    DateDescribed = Column(DATETIME2)
    DateTimeCompleted = Column(DATETIME2)
    DateTimeSampled = Column(DATETIME2)
    DepthBase = Column(DECIMAL(9, 3))
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Description = Column(Unicode(4000))
    DescriptionBy = Column(Unicode(4000))
    Diameter = Column(DECIMAL(19, 10))
    Duration = Column(BigInteger)
    GasFlowRate = Column(DECIMAL(19, 10))
    GasPressure = Column(DECIMAL(19, 10))
    Matrix = Column(Unicode(255))
    Method = Column(Unicode(255))
    Preparation = Column(Unicode(255))
    QAType = Column(Unicode(255))
    Reason = Column(Unicode(255))
    Recovery = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SampleContainer = Column(Unicode(255))
    SampleID = Column(Unicode(255), index=True)
    Sampler = Column(Unicode(255))
    SampleRecordLink = Column(Unicode(255))
    SampleReference = Column(Unicode(255), index=True)
    SpecimenCondition = Column(Unicode(255))
    StratumReference = Column(Unicode(255))
    Temperature = Column(DECIMAL(19, 10))
    Type = Column(UNIQUEIDENTIFIER, index=True)
    WaterDepth = Column(Unicode(50))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORSchmidtReboundHardnes(Base):
    __tablename__ = 'COR_SchmidtReboundHardness'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    ClampingMethod = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    HammerOrientation = Column(Unicode(255))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SchmidtHardness = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORShearBoxDatum(Base):
    __tablename__ = 'COR_ShearBoxData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    BulkDensityInitial = Column(DECIMAL(19, 10))
    CriterionUsed = Column(Unicode(255))
    Diameter = Column(DECIMAL(19, 10))
    DiameterPerpendicular = Column(DECIMAL(19, 10))
    DryDensityInitial = Column(DECIMAL(19, 10))
    MoistureContentFinal = Column(DECIMAL(19, 10))
    MoistureContentInitial = Column(DECIMAL(19, 10))
    NormalStress = Column(DECIMAL(19, 10))
    NumberOfTraverses = Column(DECIMAL(19, 10))
    ParticleDensity = Column(DECIMAL(19, 10))
    PeakShearStress = Column(DECIMAL(19, 10))
    PeakStressDisplacementRate = Column(DECIMAL(19, 10))
    PeakStressHorizontalDisplacement = Column(DECIMAL(19, 10))
    PeakStressVerticalDisplacement = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    ResidualShearStress = Column(DECIMAL(19, 10))
    ResidualStressDisplacementRate = Column(DECIMAL(19, 10))
    ResidualStressHorizontalDisplacement = Column(DECIMAL(19, 10))
    ResidualStressVerticalDisplacement = Column(DECIMAL(19, 10))
    SpecimenHeight = Column(DECIMAL(19, 10))
    TestNumber = Column(Unicode(255), index=True)
    ParticleDensityMethod = Column(UNIQUEIDENTIFIER, index=True)
    VoidsRatioInitial = Column(DECIMAL(19, 10))
    ShearBoxGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORShearBoxGeneral(Base):
    __tablename__ = 'COR_ShearBoxGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    EncapsulationMethod = Column(Unicode(255))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    PeakAngleOfFriction = Column(DECIMAL(19, 10))
    PeakCohesionIntercept = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    ResidualAngleOfFriction = Column(DECIMAL(19, 10))
    ResidualCohesionIntercept = Column(DECIMAL(19, 10))
    SpecimenConditionStatement = Column(Unicode(255))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SpecimenCondition = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORShoreScleroscopeHardnes(Base):
    __tablename__ = 'COR_ShoreScleroscopeHardness'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    AverageShoreHardnessValue = Column(DECIMAL(19, 10))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    NumberOfTests = Column(DECIMAL(19, 10))
    Orientation = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORShrinkSwell(Base):
    __tablename__ = 'COR_ShrinkSwell'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(50))
    AirVoids = Column(Unicode(50))
    AssociatedFileReference = Column(Unicode(50))
    BulkDensityInitial = Column(Unicode(50))
    CrackingRemarks = Column(Unicode(4000))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DryDensityInitial = Column(Unicode(50))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContentShrink = Column(DECIMAL(19, 10))
    MoistureContentSwell = Column(DECIMAL(19, 10))
    ParticleDensity = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    ShrinkSwellIndex = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(50))
    SpecimenReference = Column(Unicode(50), index=True)
    Status = Column(Unicode(50))
    ParticleDensityMethod = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORShrinkageLimit(Base):
    __tablename__ = 'COR_ShrinkageLimit'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    InitialDensity = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContentInitial = Column(DECIMAL(19, 10))
    PercentagePassing = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    Shrinkagelimit = Column(DECIMAL(19, 10))
    ShrinkageRatio = Column(DECIMAL(19, 10))
    SizePassing = Column(DECIMAL(19, 10))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORSlakeDurabilityIndex(Base):
    __tablename__ = 'COR_SlakeDurabilityIndex'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    FragmentAppearancePassing = Column(Unicode(255))
    FragmentAppearanceRetained = Column(Unicode(255))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SlakeDurabilityIndex1 = Column(DECIMAL(19, 10))
    SlakeDurabilityIndex2 = Column(DECIMAL(19, 10))
    SlakingFluid = Column(Unicode(255))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORSoakawayDatum(Base):
    __tablename__ = 'COR_SoakawayData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthWater = Column(Unicode(50))
    Remarks = Column(Unicode(4000))
    TimeElapsed = Column(BigInteger, index=True)
    SoakawayGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORSoakawayGeneral(Base):
    __tablename__ = 'COR_SoakawayGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DateTest = Column(DATETIME2)
    DepthEnd = Column(DECIMAL(9, 3))
    DepthStart = Column(DECIMAL(9, 3))
    Diameter = Column(DECIMAL(19, 10))
    Duration = Column(BigInteger)
    FillPorosity = Column(DECIMAL(19, 10))
    Method = Column(Unicode(255))
    OrganisationName = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SoakawayConstruction = Column(Unicode(255))
    SoakawayPitLength = Column(DECIMAL(19, 10))
    SoakawayPitWidth = Column(DECIMAL(19, 10))
    SoilInfiltrationRate = Column(DECIMAL(28, 19))
    Status = Column(Unicode(255))
    TestNumber = Column(Unicode(255), index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORStaticConeDissipationDatum(Base):
    __tablename__ = 'COR_StaticConeDissipationData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    ConeResistance = Column(DECIMAL(19, 10))
    FacePorewaterPressure = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    ShoulderPorewaterPressure = Column(DECIMAL(19, 10))
    TimeElapsed = Column(DECIMAL(19, 10), index=True)
    TopOfSleevePorewaterPressure = Column(DECIMAL(19, 10))
    StaticConeDissipationGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORStaticConeDissipationGeneral(Base):
    __tablename__ = 'COR_StaticConeDissipationGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DegreeOfDissipation = Column(DECIMAL(19, 10))
    Depth = Column(DECIMAL(9, 3), index=True)
    DissipationTime = Column(DECIMAL(19, 10))
    EquilibriumPorewaterPressure = Column(DECIMAL(19, 10))
    HorizontalCoefficientofconsolidation = Column(DECIMAL(19, 10))
    HorizontalMethod = Column(Unicode(255))
    PorePressureInitial = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    Status = Column(Unicode(255))
    VerticalCoefficientofconsolidation = Column(DECIMAL(19, 10))
    VerticalMethod = Column(Unicode(255))
    StaticConePenetrationGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORStaticConePenetrationDatum(Base):
    __tablename__ = 'COR_StaticConePenetrationData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    BulkDensity = Column(DECIMAL(19, 10))
    Conductivity = Column(DECIMAL(19, 10))
    ConeResistance = Column(DECIMAL(19, 10))
    CorrectedConeResistance = Column(DECIMAL(19, 10))
    CorrectedFrictionRatio = Column(DECIMAL(19, 10))
    CorrectedSleeveResistance = Column(DECIMAL(19, 10))
    Depth = Column(DECIMAL(9, 3), index=True)
    EffectiveConeResistance = Column(DECIMAL(19, 10))
    Effectiveverticalstress = Column(DECIMAL(19, 10))
    ExcessPorePressure = Column(DECIMAL(19, 10))
    FacePorewaterPressure = Column(DECIMAL(19, 10))
    FrictionRatio = Column(DECIMAL(19, 10))
    InSituPorePressure = Column(DECIMAL(19, 10))
    LocalUnitSideFrictionResistance = Column(DECIMAL(19, 10))
    MagneticFluxTotal = Column(DECIMAL(19, 10))
    MagneticFluxX = Column(DECIMAL(19, 10))
    MagneticFluxY = Column(DECIMAL(19, 10))
    MagneticFluxZ = Column(DECIMAL(19, 10))
    NaturalGammaRadiation = Column(DECIMAL(19, 10))
    NetConeResistance = Column(DECIMAL(19, 10))
    NormalisedConeResistance = Column(DECIMAL(19, 10))
    NormalisedFrictionRatio = Column(DECIMAL(19, 10))
    pH = Column(DECIMAL(19, 10))
    PorePressureRatio = Column(DECIMAL(19, 10))
    RedoxPotential = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    ShoulderPorewaterPressure = Column(DECIMAL(19, 10))
    SlopeIndicator1 = Column(DECIMAL(19, 10))
    SlopeIndicator2 = Column(DECIMAL(19, 10))
    SoilMoisture = Column(DECIMAL(19, 10))
    Temperature = Column(DECIMAL(19, 10))
    TopOfSleevePorewaterPressure = Column(DECIMAL(19, 10))
    TotalVerticalStress = Column(DECIMAL(19, 10))
    StaticConePenetrationGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    FI = Column(DECIMAL(12, 3))
    FID = Column(DECIMAL(12, 3))
    PhtotoMultiplier = Column(Integer)
    PID = Column(DECIMAL(12, 3))


class CORStaticConePenetrationDerivedParameter(Base):
    __tablename__ = 'COR_StaticConePenetrationDerivedParameters'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    EquivalentSPTN60 = Column(DECIMAL(19, 10))
    InternalFrictionAngle = Column(DECIMAL(19, 10))
    Interpretationreference = Column(Unicode(255), index=True)
    InterpretedSoilType = Column(Unicode(255))
    RelativeDensity = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SoilBehaviourTypeIndex = Column(DECIMAL(19, 10))
    UndrainedShearStrength = Column(DECIMAL(19, 10))
    StaticConePenetrationGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORStaticConePenetrationGeneral(Base):
    __tablename__ = 'COR_StaticConePenetrationGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    ConeAreaRatio = Column(DECIMAL(19, 10))
    ConeReference = Column(Unicode(255))
    DepthGroundwater = Column(DECIMAL(9, 3))
    DepthWaterOriginal = Column(Unicode(255))
    FilterMaterial = Column(Unicode(255))
    FrictionReducerUsed = Column(BIT)
    Method = Column(Unicode(255))
    NominalRateOfPenetration = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SleeveAreaRatio = Column(DECIMAL(19, 10))
    Subcontractor = Column(Unicode(255))
    SurfaceArea = Column(DECIMAL(19, 10))
    TestNumber = Column(Unicode(255), index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    Weather = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORStratumDetailDescription(Base):
    __tablename__ = 'COR_StratumDetailDescriptions'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Description = Column(Unicode(4000))
    Remarks = Column(Unicode(4000))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORStratumDetail(Base):
    __tablename__ = 'COR_StratumDetails'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Description = Column(Unicode(4000))
    Geologicalformation = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    StratumReference = Column(Unicode(255))
    BGSLexicon = Column(UNIQUEIDENTIFIER, index=True)
    GeologyCode = Column(UNIQUEIDENTIFIER, index=True)
    GeologyCode2 = Column(UNIQUEIDENTIFIER, index=True)
    LegendCode = Column(UNIQUEIDENTIFIER, index=True)
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    BoundaryCondition = Column(UNIQUEIDENTIFIER)


class CORSuction(Base):
    __tablename__ = 'COR_Suction'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BulkDensityInitial = Column(DECIMAL(19, 10))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    DryDensityInitial = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    MoistureContentInitial = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenLength = Column(DECIMAL(19, 10))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    Suction = Column(DECIMAL(19, 10))
    SpecimenCondition = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORSwellingIndex(Base):
    __tablename__ = 'COR_SwellingIndex'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    BulkDensityInitial = Column(DECIMAL(19, 10))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    DryDensityInitial = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenHeight = Column(DECIMAL(19, 10))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SwellingPressureIndex = Column(DECIMAL(19, 10))
    SwellingStrainIndex = Column(DECIMAL(19, 10))
    WaterContentInitial = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORTenPerCentFine(Base):
    __tablename__ = 'COR_TenPerCentFines'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    TenPercentFinesDry = Column(Unicode(255))
    TenPercentFinesWet = Column(Unicode(255))
    TestNumber = Column(Unicode(255))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORTensileStrength(Base):
    __tablename__ = 'COR_TensileStrength'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    FailureMode = Column(Unicode(255))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenCondition = Column(Unicode(255))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenHeight = Column(DECIMAL(19, 10))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    StressRate = Column(DECIMAL(19, 10))
    TensileStrength = Column(DECIMAL(19, 10))
    TestDuration = Column(BigInteger)
    TestingMachine = Column(Unicode(255))
    WaterContentSpecimen = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORTestType(Base):
    __tablename__ = 'COR_TestType'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    TestName = Column(Unicode(255), index=True)
    TestCode = Column(Unicode(255))
    Description = Column(Unicode(255))
    TestInstructions = Column(Unicode(255))
    Category = Column(UNIQUEIDENTIFIER, index=True)
    Laboratory = Column(UNIQUEIDENTIFIER, index=True)
    TestOrder = Column(DECIMAL(19, 10))


class CORTestingSchedule(Base):
    __tablename__ = 'COR_TestingSchedule'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DateDue = Column(DATETIME2)
    DateIssue = Column(DATETIME2)
    ExternalCustomerReference = Column(Unicode(255))
    ExternalReference = Column(Unicode(255))
    PreparedBy = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    ScheduleReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    ScheduleType = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    Laboratory = Column(UNIQUEIDENTIFIER, index=True)


class CORTestingScheduleDetail(Base):
    __tablename__ = 'COR_TestingScheduleDetails'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    COCReference = Column(Unicode(255))
    DateCompleted = Column(DATETIME2)
    DateDue = Column(DATETIME2)
    DependentOptions = Column(Unicode(255))
    Details = Column(Unicode(4000))
    Method = Column(Unicode(255))
    Preparation = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    Testmethod = Column(Unicode(255))
    TestName = Column(Unicode(255), index=True)
    Status = Column(UNIQUEIDENTIFIER, index=True)
    TestingSchedule = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    TestCount = Column(Integer)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)


class CORTimeRelatedRemarksLocation(Base):
    __tablename__ = 'COR_TimeRelatedRemarksLocation'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DateTimeEnd = Column(DATETIME2)
    DateTimeStart = Column(DATETIME2, index=True)
    Duration = Column(BigInteger)
    Remarks = Column(Unicode(4000))
    SubLocation = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORTimeRelatedRemarksProject(Base):
    __tablename__ = 'COR_TimeRelatedRemarksProject'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DateTimeEnd = Column(DATETIME2)
    DateTimeStart = Column(DATETIME2, index=True)
    Duration = Column(BigInteger)
    Remarks = Column(Unicode(4000))
    SubLocation = Column(Unicode(255))
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORTriaxialEffectiveStressDatum(Base):
    __tablename__ = 'COR_TriaxialEffectiveStressData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    AxialStrainRate = Column(DECIMAL(19, 10))
    BulkDensityInitial = Column(DECIMAL(19, 10))
    CellPressure = Column(DECIMAL(19, 10))
    ConsolidationStage = Column(Unicode(255))
    Diameter = Column(DECIMAL(19, 10))
    DryDensityInitial = Column(DECIMAL(19, 10))
    EffectiveStressEnd = Column(DECIMAL(19, 10))
    FailureAxialStrain = Column(DECIMAL(19, 10))
    FailureDeviatorStress = Column(DECIMAL(19, 10))
    FailureMode = Column(Unicode(255))
    FailurePorePressure = Column(DECIMAL(19, 10))
    FailureVolumetricStrain = Column(DECIMAL(19, 10))
    InitialPorePressure = Column(DECIMAL(19, 10))
    MoistureContentFinal = Column(DECIMAL(19, 10))
    MoistureContentInitial = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    Saturation = Column(Unicode(255))
    SpecimenLength = Column(DECIMAL(19, 10))
    TestNumber = Column(Unicode(255), index=True)
    TriaxialEffectiveStressGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORTriaxialEffectiveStressGeneral(Base):
    __tablename__ = 'COR_TriaxialEffectiveStressGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    CohesionIntercept = Column(DECIMAL(19, 10))
    Cu = Column(DECIMAL(19, 10))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    FailureCriterion = Column(Unicode(255))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Phi = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SpecimenCondition = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORTriaxialTotalStressDatum(Base):
    __tablename__ = 'COR_TriaxialTotalStressData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    BulkDensityInitial = Column(DECIMAL(19, 10))
    CellPressure = Column(DECIMAL(19, 10))
    Diameter = Column(DECIMAL(19, 10))
    DryDensityInitial = Column(DECIMAL(19, 10))
    FailureAxialStrain = Column(DECIMAL(19, 10))
    FailureCorrectedDeviatorStress = Column(DECIMAL(19, 10))
    FailureMode = Column(Unicode(255))
    FailureShearStrength = Column(DECIMAL(19, 10))
    MoistureContentFinal = Column(DECIMAL(19, 10))
    MoistureContentInitial = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenLength = Column(DECIMAL(19, 10))
    TestNumber = Column(Unicode(255), index=True)
    TriaxialTotalStressGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORTriaxialTotalStressGeneral(Base):
    __tablename__ = 'COR_TriaxialTotalStressGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    CohesionIntercept = Column(DECIMAL(19, 10))
    Cu = Column(DECIMAL(19, 10))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Phi = Column(DECIMAL(19, 10))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    SpecimenCondition = Column(UNIQUEIDENTIFIER, index=True)
    TestType = Column(UNIQUEIDENTIFIER, index=True)
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORWaterAdded(Base):
    __tablename__ = 'COR_WaterAdded'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    WaterAdded = Column(DECIMAL(19, 10))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORWaterContentOfRock(Base):
    __tablename__ = 'COR_WaterContentOfRock'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AccreditionReference = Column(Unicode(255))
    AssociatedFileReference = Column(Unicode(255))
    DepthSpecimenTop = Column(DECIMAL(9, 3), index=True)
    DryingTemperature = Column(DECIMAL(19, 10))
    LaboratoryName = Column(Unicode(255))
    Method = Column(Unicode(255))
    Remarks = Column(Unicode(4000))
    SpecimenDescription = Column(Unicode(4000))
    SpecimenPreparation = Column(Unicode(255))
    SpecimenReference = Column(Unicode(255), index=True)
    Status = Column(Unicode(255))
    WaterContent = Column(DECIMAL(19, 10))
    SampleInformation = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORWaterStrikeDetail(Base):
    __tablename__ = 'COR_WaterStrikeDetails'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthWater = Column(Unicode(50))
    Remarks = Column(Unicode(4000))
    TimeElapsed = Column(DECIMAL(19, 10), index=True)
    WaterStrikeGeneral = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    DepthWaterValue = Column(DECIMAL(12, 3))


class CORWaterStrikeGeneral(Base):
    __tablename__ = 'COR_WaterStrikeGeneral'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DateTime = Column(DATETIME2)
    DepthCasing = Column(DECIMAL(9, 3))
    DepthSealed = Column(DECIMAL(9, 3))
    DepthStrike = Column(DECIMAL(9, 3), index=True)
    Remarks = Column(Unicode(4000))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORWeathering(Base):
    __tablename__ = 'COR_Weathering'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Remarks = Column(Unicode(4000))
    WeatheringScheme = Column(UNIQUEIDENTIFIER, index=True)
    WeatheringSystemType = Column(UNIQUEIDENTIFIER, index=True)
    WeatheringClassification = Column(Unicode(255))
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CORWindowSampling(Base):
    __tablename__ = 'COR_WindowSampling'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DATETIME2, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    AssociatedFileReference = Column(Unicode(255))
    DepthBase = Column(DECIMAL(9, 3), index=True)
    DepthTop = Column(DECIMAL(9, 3), index=True)
    Diameter = Column(DECIMAL(19, 10))
    Duration = Column(BigInteger)
    Remarks = Column(Unicode(4000))
    SampleRecovery = Column(DECIMAL(19, 10))
    TestNumber = Column(Unicode(255), index=True)
    LocationDetails = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class CPMCivilElementTerm(Base):
    __tablename__ = 'CPM_CivilElementTerm'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    ElementName = Column(Unicode(255))
    Term = Column(Unicode(255))
    KeyId = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)


class CPMCivilLayerNamingPattern(Base):
    __tablename__ = 'CPM_CivilLayerNamingPattern'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Prefix = Column(Unicode(255))
    Suffix = Column(Unicode(255))
    RefineByHatch = Column(BIT)
    Component1 = Column(Unicode(255))
    Component2 = Column(Unicode(255))
    Component3 = Column(Unicode(255))
    Delimiter1 = Column(Unicode(255))
    Delimiter2 = Column(Unicode(255))
    KeyId = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)


class CPMCivilObjectTerm(Base):
    __tablename__ = 'CPM_CivilObjectTerm'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    ObjectName = Column(Unicode(255))
    Term = Column(Unicode(255))
    KeyId = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)


class CPMConfigPack(Base):
    __tablename__ = 'CPM_ConfigPack'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    Name = Column(Unicode(255))
    DateCreate = Column(DateTime)
    IsActive = Column(BIT)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    SourceConfigPack = Column(UNIQUEIDENTIFIER)
    Author = Column(Unicode(255))
    Region = Column(Unicode(255))
    KeyName = Column(Unicode(255))
    HBSIVersion = Column(Unicode(255))


class CPMDataEntryGridPositionDefinition(Base):
    __tablename__ = 'CPM_DataEntryGridPositionDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    IsActive = Column(BIT)
    IsController = Column(BIT)
    Type = Column(Unicode(255))
    Order = Column(DECIMAL(9, 2), index=True)
    GridDefinition = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, nullable=False, index=True, server_default=text("(newsequentialid())"))
    DataEntryStepDefinition = Column(UNIQUEIDENTIFIER, index=True)


class CPMDataEntryProfileDefinition(Base):
    __tablename__ = 'CPM_DataEntryProfileDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Name = Column(Unicode(255))
    IsActive = Column(BIT)
    KeyId = Column(UNIQUEIDENTIFIER, nullable=False, index=True, server_default=text("(newsequentialid())"))


class CPMDataEntryStepDefinition(Base):
    __tablename__ = 'CPM_DataEntryStepDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    IsActive = Column(BIT)
    Name = Column(Unicode(255))
    Order = Column(DECIMAL(9, 2), index=True)
    DataEntryProfileDefinition = Column(UNIQUEIDENTIFIER, index=True)
    LocationGridDefinition = Column(UNIQUEIDENTIFIER)
    KeyId = Column(UNIQUEIDENTIFIER, nullable=False, index=True, server_default=text("(newsequentialid())"))


class CPMEntityDefinition(Base):
    __tablename__ = 'CPM_EntityDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    EntityName = Column(Unicode(255), index=True)
    IsCustom = Column(BIT)
    IsActive = Column(BIT)
    Title = Column(Unicode(255))
    IsView = Column(BIT)
    Description = Column(Unicode(4000))
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    AGS_Name = Column(Unicode(50))
    KeyId = Column(UNIQUEIDENTIFIER, index=True, server_default=text("(newsequentialid())"))
    IsDepthJoinTarget = Column(BIT)
    CanCreateRole = Column(UNIQUEIDENTIFIER)
    CanEditRole = Column(UNIQUEIDENTIFIER)
    CanDeleteRole = Column(UNIQUEIDENTIFIER)


class CPMExpressionDefinition(Base):
    __tablename__ = 'CPM_ExpressionDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255))
    EntityName = Column(Unicode(255))
    Description = Column(Unicode(255))
    Expression = Column(Unicode(2400))
    IsActive = Column(BIT)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, index=True, server_default=text("(newsequentialid())"))


class CPMFilter(Base):
    __tablename__ = 'CPM_Filter'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    EntityName = Column(Unicode(255), nullable=False)
    PropertyName = Column(Unicode(255), nullable=False)
    Operator = Column(Unicode(255), nullable=False)
    Type = Column(Unicode(255))
    Value = Column(Unicode(255))
    FilterGroup_id = Column(UNIQUEIDENTIFIER, nullable=False)
    Index = Column(Integer)


class CPMFilterGroup(Base):
    __tablename__ = 'CPM_FilterGroup'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    And = Column(BIT, nullable=False)
    FilterGroup_id = Column(UNIQUEIDENTIFIER)
    Index = Column(Integer)


class CPMFormDefinition(Base):
    __tablename__ = 'CPM_FormDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    EntityName = Column(Unicode(255))
    Name = Column(Unicode(255))


class CPMFormFieldDefinition(Base):
    __tablename__ = 'CPM_FormFieldDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Availability = Column(Unicode(255))
    DefaultValue = Column(Unicode(255))
    EntityName = Column(Unicode(255))
    Header = Column(Unicode(255))
    Index = Column(DECIMAL(19, 5))
    IsReadonly = Column(BIT)
    PropertyName = Column(Unicode(255))
    SectionName = Column(Unicode(255))
    Visibility = Column(Unicode(255))
    FormDefinitionId = Column(UNIQUEIDENTIFIER, index=True)


class CPMGeologyLineStyleDefinition(Base):
    __tablename__ = 'CPM_GeologyLineStyleDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    Name = Column(Unicode(255))
    LinePattern = Column(Unicode(255))
    LineWeight = Column(Unicode(255))
    LineColourAlpha = Column(TINYINT)
    LineColourRed = Column(TINYINT)
    LineColourGreen = Column(TINYINT)
    LineColourBlue = Column(TINYINT)
    IsActive = Column(BIT)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)
    Snapshot = Column(UNIQUEIDENTIFIER)
    KeyId = Column(UNIQUEIDENTIFIER)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))


class CPMGeotechnicalHatch(Base):
    __tablename__ = 'CPM_GeotechnicalHatch'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255), nullable=False, index=True)
    IsProtected = Column(BIT, nullable=False)
    Colour = Column(Integer, nullable=False)
    Category = Column(Unicode(255), index=True)
    Description = Column(Unicode(255))
    CreatedBy = Column(UNIQUEIDENTIFIER)
    CreatedOn = Column(DateTime, nullable=False)
    KeyId = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Material = Column(Unicode(255))


class CPMGeotechnicalHatchComponent(Base):
    __tablename__ = 'CPM_GeotechnicalHatchComponent'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Order = Column(Integer, index=True)
    HatchName = Column(Unicode(255), nullable=False)
    HatchPatternType = Column(Integer)
    Colour = Column(Integer, nullable=False)
    Angle = Column(DECIMAL(19, 5))
    Scale = Column(DECIMAL(19, 5))
    GeotechnicalHatch = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)


class CPMGeotechnicalPlanStripStyle(Base):
    __tablename__ = 'CPM_GeotechnicalPlanStripStyle'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255), nullable=False)
    HeaderStyleName = Column(Unicode(255))
    TemplateDocumentName = Column(Unicode(255))
    XOffset = Column(DECIMAL(19, 5), nullable=False)
    YOffset = Column(DECIMAL(19, 5), nullable=False)
    ShowLeaderLine = Column(BIT, nullable=False)
    IsProtected = Column(BIT, nullable=False)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    CreatedOn = Column(DateTime, nullable=False)
    StripScale = Column(DECIMAL(19, 5))
    TextScale = Column(DECIMAL(19, 5))
    KeyId = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)


class CPMGeotechnicalStickStyle(Base):
    __tablename__ = 'CPM_GeotechnicalStickStyle'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255), nullable=False)
    Diameter = Column(DECIMAL(19, 5), nullable=False)
    IsProtected = Column(BIT, nullable=False)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    CreatedOn = Column(DateTime, nullable=False)
    KeyId = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)


class CPMGeotechnicalStripStyle(Base):
    __tablename__ = 'CPM_GeotechnicalStripStyle'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255), nullable=False)
    HeaderStyleName = Column(Unicode(255))
    TemplateDocumentName = Column(Unicode(255))
    IsProtected = Column(BIT, nullable=False)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    CreatedOn = Column(DateTime, nullable=False)
    StripScale = Column(DECIMAL(19, 5))
    TextScale = Column(DECIMAL(19, 5))
    KeyId = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)


class CPMGeotechnicalStyle(Base):
    __tablename__ = 'CPM_GeotechnicalStyle'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Type = Column(Unicode(255))
    PointStyle = Column(Unicode(255))
    LabelStyle = Column(Unicode(255))
    StickStyle3d = Column(UNIQUEIDENTIFIER)
    StripStyle2d = Column(UNIQUEIDENTIFIER)
    GeotechnicalStyleGroup = Column(UNIQUEIDENTIFIER, index=True)
    PlanStripStyle2d = Column(UNIQUEIDENTIFIER)
    KeyId = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)


class CPMGeotechnicalStyleGroup(Base):
    __tablename__ = 'CPM_GeotechnicalStyleGroup'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255), nullable=False, index=True)
    IsProtected = Column(BIT, nullable=False)
    DefaultStyle = Column(UNIQUEIDENTIFIER, nullable=False)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    CreatedOn = Column(DateTime, nullable=False)
    KeyId = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)


class CPMGraphSeriesStyleDefinition(Base):
    __tablename__ = 'CPM_GraphSeriesStyleDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    Name = Column(Unicode(255))
    LinePattern = Column(Unicode(255))
    LineColourRed = Column(TINYINT)
    LineColourGreen = Column(TINYINT)
    LineColourBlue = Column(TINYINT)
    MarkerFillRed = Column(TINYINT)
    MarkerFillGreen = Column(TINYINT)
    MarkerFillBlue = Column(TINYINT)
    MarkerOutlineRed = Column(TINYINT)
    MarkerOutlineGreen = Column(TINYINT)
    MarkerOutlineBlue = Column(TINYINT)
    MarkerStyle = Column(Unicode(255))
    IsActive = Column(BIT)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)
    Snapshot = Column(UNIQUEIDENTIFIER)
    KeyId = Column(UNIQUEIDENTIFIER)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))


class CPMGridColumnDefinition(Base):
    __tablename__ = 'CPM_GridColumnDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Availability = Column(Unicode(255))
    DefaultValue = Column(Unicode(255))
    EntityName = Column(Unicode(255))
    Header = Column(Unicode(255))
    Index = Column(DECIMAL(19, 5))
    IsFilterable = Column(BIT)
    IsGroupable = Column(BIT)
    IsReadonly = Column(BIT)
    IsSortable = Column(BIT)
    PropertyName = Column(Unicode(255))
    Visibility = Column(Unicode(255))
    GridDefinitionId = Column(UNIQUEIDENTIFIER, index=True)


class CPMGridDefinition(Base):
    __tablename__ = 'CPM_GridDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    EntityName = Column(Unicode(255))
    IsDataEntryGrid = Column(BIT)
    Name = Column(Unicode(255))
    IsReadOnly = Column(BIT)


class CPMGrouping(Base):
    __tablename__ = 'CPM_Grouping'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    EntityName = Column(Unicode(255), nullable=False)
    PropertyName = Column(Unicode(255), nullable=False)
    Aggregate = Column(Unicode(255))
    SearchDefinition_id = Column(UNIQUEIDENTIFIER, nullable=False)
    Index = Column(Integer)


class CPMLogReportProfile(Base):
    __tablename__ = 'CPM_LogReportProfile'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Name = Column(Unicode(255), index=True)
    CreatedOn = Column(DATETIME2)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    KeyId = Column(UNIQUEIDENTIFIER)


class CPMLogReportTemplate(Base):
    __tablename__ = 'CPM_LogReportTemplate'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Document = Column(UNIQUEIDENTIFIER)
    Scale = Column(UNIQUEIDENTIFIER)
    Orientation = Column(Unicode(255))
    PaperSize = Column(UNIQUEIDENTIFIER)
    Order = Column(Integer, index=True)
    Type = Column(UNIQUEIDENTIFIER, index=True)
    LogReportProfile = Column(UNIQUEIDENTIFIER, index=True)
    MasterTemplateStripSet = Column(UNIQUEIDENTIFIER, index=True)
    UnitsPerPage = Column(Integer)


class CPMMapCoordinateSystem(Base):
    __tablename__ = 'CPM_MapCoordinateSystem'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Crs = Column(Unicode(255))
    Name = Column(Unicode(255))
    Proj = Column(Unicode(2400))
    IsActive = Column(BIT)


class CPMMapDefinition(Base):
    __tablename__ = 'CPM_MapDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    InitialLatitude = Column(DECIMAL(19, 5))
    InitialLongitude = Column(DECIMAL(19, 5))
    InitialZoomScale = Column(Integer)
    Name = Column(Unicode(255))
    MapCoordinateSystem = Column(UNIQUEIDENTIFIER)


class CPMMapLayerDefinition(Base):
    __tablename__ = 'CPM_MapLayerDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Type = Column(Unicode(255), nullable=False)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    MaximumMapZoomLevel = Column(Unicode(255))
    MinimumMapZoomLevel = Column(Unicode(255))
    Name = Column(Unicode(255))
    IsCached = Column(BIT)
    MapDatasetIndex = Column(UNIQUEIDENTIFIER)
    IsSelectionLayer = Column(BIT)
    LocationGroup = Column(UNIQUEIDENTIFIER)
    SearchDefinition = Column(UNIQUEIDENTIFIER)
    HttpBasicPassword = Column(Unicode(255))
    HttpBasicUsername = Column(Unicode(255))
    Opacity = Column(TINYINT)
    Uri = Column(Unicode(4000))
    ExpiryDate = Column(DATETIME2)


class CPMMapLayerTheme(Base):
    __tablename__ = 'CPM_MapLayerTheme'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Type = Column(Unicode(255), nullable=False)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Name = Column(Unicode(255))
    MapLayerDefinition = Column(UNIQUEIDENTIFIER)
    MaximumMapZoomLevel = Column(Unicode(255))
    MinimumMapZoomLevel = Column(Unicode(255))
    Order = Column(DECIMAL(19, 5))
    Colour = Column(Unicode(6))
    HatchStyle = Column(Unicode(255))
    Opacity = Column(TINYINT)
    OutlineColour = Column(Unicode(6))
    OutlineOpacity = Column(TINYINT)
    OutlinePatternStyle = Column(Unicode(255))
    OutlineSize = Column(DECIMAL(19, 5))
    OutlineSizeUnit = Column(Unicode(255))
    ToolTipMapLayerTheme = Column(UNIQUEIDENTIFIER)
    Aggregate = Column(Unicode(255))
    Entity = Column(Unicode(255))
    Offset = Column(DECIMAL(19, 5))
    OffsetPosition = Column(Unicode(255))
    OffsetUnit = Column(Unicode(255))
    Property = Column(Unicode(255))
    RotationProperty = Column(Unicode(255))
    Size = Column(DECIMAL(19, 5))
    SizeUnit = Column(Unicode(255))
    Cap = Column(Unicode(255))
    PatternStyle = Column(Unicode(255))
    SymbolType = Column(Unicode(255))


class CPMMapLayerThemeCondition(Base):
    __tablename__ = 'CPM_MapLayerThemeCondition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Type = Column(Unicode(255), nullable=False)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Aggregate = Column(Unicode(255))
    Entity = Column(Unicode(255))
    Property = Column(Unicode(255))
    MapLayerTheme = Column(UNIQUEIDENTIFIER)
    Value = Column(Unicode(255))
    Maximum = Column(DECIMAL(19, 5))
    Minimum = Column(DECIMAL(19, 5))


class CPMMapLayerThemeToolTip(Base):
    __tablename__ = 'CPM_MapLayerThemeToolTip'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Type = Column(Unicode(255), nullable=False)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Format = Column(Unicode(255))
    Name = Column(Unicode(255))
    Order = Column(DECIMAL(19, 5))
    MapLayerTheme = Column(UNIQUEIDENTIFIER)
    Aggregate = Column(Unicode(255))
    Entity = Column(Unicode(255))
    Property = Column(Unicode(255))
    Column = Column(Unicode(255))
    XPath = Column(Unicode(255))


class CPMMapLegendGroup(Base):
    __tablename__ = 'CPM_MapLegendGroup'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    InitiallyVisible = Column(BIT)
    Order = Column(DECIMAL(19, 5))
    MapDefinition = Column(UNIQUEIDENTIFIER)
    MapLayerDefinition = Column(UNIQUEIDENTIFIER)


class CPMMasterTemplateStripSet(Base):
    __tablename__ = 'CPM_MasterTemplateStripSet'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Name = Column(Unicode(255))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)
    KeyID = Column(UNIQUEIDENTIFIER, server_default=text("(newsequentialid())"))


class CPMMasterTemplateStripSetLink(Base):
    __tablename__ = 'CPM_MasterTemplateStripSetLink'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    MasterTemplate = Column(UNIQUEIDENTIFIER, index=True)
    MasterTemplateStripSet = Column(UNIQUEIDENTIFIER, index=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)
    KeyID = Column(UNIQUEIDENTIFIER, server_default=text("(newsequentialid())"))


class CPMMasterTemplateStripSetPickListLink(Base):
    __tablename__ = 'CPM_MasterTemplateStripSetPickListLink'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    MasterTemplateStripSet = Column(UNIQUEIDENTIFIER, index=True)
    PickList = Column(UNIQUEIDENTIFIER, index=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)
    KeyID = Column(UNIQUEIDENTIFIER, server_default=text("(newsequentialid())"))


class CPMMasterTemplateStripSetStripLink(Base):
    __tablename__ = 'CPM_MasterTemplateStripSetStripLink'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    MasterTemplateStripSet = Column(UNIQUEIDENTIFIER, index=True)
    Strip = Column(UNIQUEIDENTIFIER, index=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)
    KeyID = Column(UNIQUEIDENTIFIER, server_default=text("(newsequentialid())"))
    Order = Column(DECIMAL(5, 2))
    Width = Column(DECIMAL(19, 10))


class CPMOptionDefinition(Base):
    __tablename__ = 'CPM_OptionDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Key = Column(Unicode(255))
    Value = Column(Unicode(255))
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)


class CPMOrdering(Base):
    __tablename__ = 'CPM_Ordering'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Ascending = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    EntityName = Column(Unicode(255), nullable=False)
    PropertyName = Column(Unicode(255), nullable=False)
    SearchDefinition_id = Column(UNIQUEIDENTIFIER, nullable=False)
    Index = Column(Integer)


class CPMPaperSize(Base):
    __tablename__ = 'CPM_PaperSize'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255), index=True)
    Width = Column(Float(53))
    Height = Column(Float(53))


class CPMPickList(Base):
    __tablename__ = 'CPM_PickList'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Value = Column(Unicode(255), index=True)
    Description = Column(Unicode(4000))
    PickListGroupDefinition = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, index=True, server_default=text("(newsequentialid())"))
    Order = Column(DECIMAL(19, 5))
    VectorSymbol = Column(UNIQUEIDENTIFIER)
    VectorSymbolTop = Column(UNIQUEIDENTIFIER)
    VectorSymbolBase = Column(UNIQUEIDENTIFIER)
    VectorSymbolConnector = Column(UNIQUEIDENTIFIER)
    GeologyLineStyleDefinition = Column(UNIQUEIDENTIFIER)


class CPMPickListAlia(Base):
    __tablename__ = 'CPM_PickListAlias'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Value = Column(Unicode(255), index=True)
    PickList = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, index=True)


class CPMPickListDefinition(Base):
    __tablename__ = 'CPM_PickListDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    EntityName = Column(Unicode(255), index=True)
    PropertyName = Column(Unicode(255), index=True)
    PickListGroupDefinition = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)


class CPMPickListGroupDefinition(Base):
    __tablename__ = 'CPM_PickListGroupDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255))
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, index=True, server_default=text("(newsequentialid())"))


class CPMPickListSetDefinition(Base):
    __tablename__ = 'CPM_PickListSetDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Name = Column(Unicode(255), index=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Description = Column(Unicode(4000))
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, index=True, server_default=text("(newsequentialid())"))


class CPMPickListSetLinkDefinition(Base):
    __tablename__ = 'CPM_PickListSetLinkDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, index=True, server_default=text("(newsequentialid())"))
    PicklistSetDefinition = Column(UNIQUEIDENTIFIER, nullable=False, index=True)
    Picklist = Column(UNIQUEIDENTIFIER, nullable=False, index=True)


class CPMPickListStyleLink(Base):
    __tablename__ = 'CPM_PickListStyleLink'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Style = Column(UNIQUEIDENTIFIER)
    PickList = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)
    KeyId = Column(UNIQUEIDENTIFIER)


class CPMPluginDefinition(Base):
    __tablename__ = 'CPM_PluginDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Name = Column(Unicode(255))
    FileName = Column(Unicode(255))
    DirectoryName = Column(Unicode(255))
    Version = Column(Unicode(255))
    OnSave = Column(BIT)
    OnLoad = Column(BIT)
    OnCreate = Column(BIT)
    EntityDefinition = Column(UNIQUEIDENTIFIER)
    IsActive = Column(BIT)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    OnBulkUpdate = Column(BIT)
    Order = Column(DECIMAL(5, 2))


class CPMPropertyDefinition(Base):
    __tablename__ = 'CPM_PropertyDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    EntityName = Column(Unicode(255), index=True)
    PropertyName = Column(Unicode(255), index=True)
    Description = Column(Unicode(255))
    NHibernateType = Column(Unicode(50))
    Size = Column(Integer)
    DecimalPlaces = Column(Integer)
    DisplayNameShort = Column(Unicode(50))
    DisplayNameLong = Column(Unicode(255))
    DisplayFormat = Column(Unicode(50))
    DisplayType = Column(Unicode(50))
    IsReference = Column(BIT)
    IsParent = Column(BIT)
    IsCollection = Column(BIT)
    IsCustom = Column(BIT)
    IsKeyColumn = Column(BIT)
    IsSystemProperty = Column(BIT, server_default=text("((0))"))
    IsActive = Column(BIT)
    IsIndexed = Column(BIT)
    IsNullable = Column(BIT)
    AGS_Name = Column(Unicode(50))
    Order = Column(DECIMAL(5, 2))
    EntityDefinition = Column(UNIQUEIDENTIFIER, index=True)
    Expression = Column(Unicode(4000))
    IsCalculatedFieldActive = Column(BIT)
    IsDepth = Column(BIT)
    IsTriggerResult = Column(BIT)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, index=True, server_default=text("(newsequentialid())"))
    UnitDefinition = Column(UNIQUEIDENTIFIER, index=True)
    IsDepthJoin = Column(BIT)
    IsBaseDepth = Column(BIT)
    IsTopDepth = Column(BIT)
    IsRestricted = Column(BIT)
    SecondaryUnitDefinition = Column(UNIQUEIDENTIFIER, index=True)


class CPMQuickListDefinition(Base):
    __tablename__ = 'CPM_QuickListDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    EntityName = Column(Unicode(255), index=True)
    PropertyName = Column(Unicode(255), index=True)
    QuickListGroupDefinition = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)


class CPMQuickListGroupDefinition(Base):
    __tablename__ = 'CPM_QuickListGroupDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255))
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, index=True)


class CPMQuickListGroupLinkDefinition(Base):
    __tablename__ = 'CPM_QuickListGroupLinkDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    QuickListGuid = Column(UNIQUEIDENTIFIER)
    PickListGuid = Column(UNIQUEIDENTIFIER)
    Ordering = Column(Integer)
    Type = Column(Unicode(255))
    Title = Column(Unicode(255))
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)
    KeyId = Column(UNIQUEIDENTIFIER)
    IsDefault = Column(BIT)


class CPMScale(Base):
    __tablename__ = 'CPM_Scale'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Numerator = Column(Integer, index=True)
    Denominator = Column(Integer, index=True)


class CPMSearchDefinition(Base):
    __tablename__ = 'CPM_SearchDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    EntityName = Column(Unicode(255))
    FirstResult = Column(Integer, nullable=False)
    IsPublic = Column(BIT)
    MaxResults = Column(Integer, nullable=False)
    Name = Column(Unicode(255))
    Owner = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    PreFilterGroup_id = Column(UNIQUEIDENTIFIER)
    FilterGroup_id = Column(UNIQUEIDENTIFIER)


t_CPM_Template_OptionDefinition = Table(
    'CPM_Template_OptionDefinition', metadata,
    Column('Id', UNIQUEIDENTIFIER, nullable=False, server_default=text("(newsequentialid())")),
    Column('Key', Unicode(255)),
    Column('Value', Unicode(255)),
    Column('ConfigPack', UNIQUEIDENTIFIER)
)


class CPMTreeNodeDefinition(Base):
    __tablename__ = 'CPM_TreeNodeDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Title = Column(Unicode(255))
    NodeType = Column(Unicode(50))
    EntityName = Column(Unicode(255))
    GridDefinitionName = Column(Unicode(255))
    Order = Column(DECIMAL(6, 2))
    ShowCount = Column(BIT)
    Expanded = Column(BIT)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Parent = Column(UNIQUEIDENTIFIER)
    SearchDefinition = Column(UNIQUEIDENTIFIER)
    KeyId = Column(UNIQUEIDENTIFIER, index=True, server_default=text("(newsequentialid())"))


class CPMTriggerLevelDefinition(Base):
    __tablename__ = 'CPM_TriggerLevelDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    IsActive = Column(BIT)
    PrimaryFilter = Column(Unicode(255))
    SecondaryFilter = Column(Unicode(255))
    TertiaryFilter = Column(Unicode(255))
    Unit = Column(UNIQUEIDENTIFIER)
    From = Column(DECIMAL(19, 10))
    To = Column(DECIMAL(19, 10))
    TriggerThemeDefinition = Column(UNIQUEIDENTIFIER)
    TriggerSetDefinition = Column(UNIQUEIDENTIFIER, nullable=False, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, index=True, server_default=text("(newsequentialid())"))


class CPMTriggerSetDefinition(Base):
    __tablename__ = 'CPM_TriggerSetDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Name = Column(Unicode(255))
    Description = Column(Unicode(4000))
    IsActive = Column(BIT)
    Order = Column(DECIMAL(9, 2), index=True)
    NotesForUsage = Column(Unicode(4000))
    EntityName = Column(Unicode(255))
    PrimaryPropertyName = Column(Unicode(255))
    SecondaryPropertyName = Column(Unicode(255))
    TertiaryPropertyName = Column(Unicode(255))
    PrimaryPropertyEntityName = Column(Unicode(255))
    SecondaryPropertyEntityName = Column(Unicode(255))
    TertiaryPropertyEntityName = Column(Unicode(255))
    TriggerValuePropertyName = Column(Unicode(255))
    TriggerUnitPropertyName = Column(Unicode(255))
    KeyId = Column(UNIQUEIDENTIFIER, index=True, server_default=text("(newsequentialid())"))


class CPMTriggerThemeDefinition(Base):
    __tablename__ = 'CPM_TriggerThemeDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    IsActive = Column(BIT)
    Code = Column(DECIMAL(9, 2))
    Description = Column(Unicode(255))
    Colour = Column(Unicode(255))
    TriggerSetDefinition = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER, index=True, server_default=text("(newsequentialid())"))


class CPMUnitDefinition(Base):
    __tablename__ = 'CPM_UnitDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Type = Column(Unicode(255))
    DisplayFormat = Column(Unicode(255))
    UnitGroup = Column(UNIQUEIDENTIFIER, index=True)
    ConversionToBaseFactor = Column(DECIMAL(28, 19))
    ConversionToBaseOffset = Column(DECIMAL(28, 19))
    DisplayType = Column(Unicode(50))


class CPMUnitGroup(Base):
    __tablename__ = 'CPM_UnitGroup'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    SnapShot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255), nullable=False, index=True)
    Description = Column(Unicode(255))
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    KeyId = Column(UNIQUEIDENTIFIER)


class CPMValidationDefinition(Base):
    __tablename__ = 'CPM_ValidationDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255))
    Description = Column(Unicode(255))
    ClassName = Column(Unicode(255))
    IsActive = Column(BIT)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)


class CPMVectorSymbol(Base):
    __tablename__ = 'CPM_VectorSymbol'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Name = Column(Unicode(255), index=True)
    XamlDrawingGroup = Column(Unicode)


class CPMViewGridDefinition(Base):
    __tablename__ = 'CPM_ViewGridDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Name = Column(Unicode(255))
    Description = Column(Unicode(255))
    ViewName = Column(Unicode(255))
    ViewHash = Column(Unicode(255))


class CPMXMLMappingDefinition(Base):
    __tablename__ = 'CPM_XMLMappingDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Name = Column(Unicode(255))
    Type = Column(Unicode(255))
    IsActive = Column(BIT)
    IsSystem = Column(BIT)


class CPMXMLMappingFieldDefinition(Base):
    __tablename__ = 'CPM_XMLMappingFieldDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Source = Column(Unicode(255))
    Destination = Column(Unicode(255))
    Key = Column(BIT)
    IsCustom = Column(BIT)
    Expression = Column(Unicode(255))
    Default = Column(Unicode(255))
    Condition = Column(Unicode(4000))
    UnitSource = Column(Unicode(255))
    SafeMerge = Column(BIT)
    ForcedType = Column(Unicode(255))
    AbbreviationSource = Column(Unicode(255))
    Type = Column(Unicode(255))
    Order = Column(DECIMAL(9, 2), index=True)
    XMLMappingRowDefinition = Column(UNIQUEIDENTIFIER)
    XMLMappingDefinition = Column(UNIQUEIDENTIFIER, index=True)


class CPMXMLMappingInputDefinition(Base):
    __tablename__ = 'CPM_XMLMappingInputDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Group = Column(Unicode(255))
    IsCustom = Column(BIT)
    Order = Column(DECIMAL(9, 2), index=True)
    XMLMappingDefinition = Column(UNIQUEIDENTIFIER)
    XMLMappingOutputDefinition = Column(UNIQUEIDENTIFIER)


class CPMXMLMappingOutputDefinition(Base):
    __tablename__ = 'CPM_XMLMappingOutputDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Group = Column(Unicode(255))
    IsCustom = Column(BIT)
    PreventDuplicates = Column(BIT)
    Order = Column(DECIMAL(9, 2), index=True)
    XMLMappingDefinition = Column(UNIQUEIDENTIFIER, index=True)
    XMLMappingInputDefinition = Column(UNIQUEIDENTIFIER, index=True)


class CPMXMLMappingRowDefinition(Base):
    __tablename__ = 'CPM_XMLMappingRowDefinition'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Condition = Column(Unicode(4000))
    Merge = Column(BIT)
    MergeOnly = Column(BIT)
    IsCustom = Column(BIT)
    Order = Column(DECIMAL(9, 2), index=True)
    XMLMappingDefinition = Column(UNIQUEIDENTIFIER, index=True)
    XMLMappingOutputDefinition = Column(UNIQUEIDENTIFIER)


t_GridView_Configurations_00000000_0000_0000_0000_000000000000 = Table(
    'GridView_Configurations_00000000_0000_0000_0000_000000000000', metadata,
    Column('ConfigPackId', UNIQUEIDENTIFIER, nullable=False),
    Column('ConfigPackName', Unicode(255)),
    Column('ConfigPackDateCreate', DateTime),
    Column('ConfigPackIsActive', BIT),
    Column('ConfigPackId_2', UNIQUEIDENTIFIER, nullable=False)
)


t_GridView_Density_Tests_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'GridView_Density Tests_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('DensityId', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationDetailsLocationID', Unicode(255)),
    Column('SampleInformationDepthTop', DECIMAL(9, 3)),
    Column('SampleInformationSampleReference', Unicode(255)),
    Column('SampleInformationuui_Type', UNIQUEIDENTIFIER),
    Column('SampleInformationSampleID', Unicode(255)),
    Column('DensitySpecimenReference', Unicode(255)),
    Column('DensityDepthSpecimenTop', DECIMAL(9, 3)),
    Column('DensitySpecimenDescription', Unicode(4000)),
    Column('DensitySpecimenPreparation', Unicode(255)),
    Column('Densityuui_TestType', UNIQUEIDENTIFIER),
    Column('Densityuui_SampleCondition', UNIQUEIDENTIFIER),
    Column('Densityuui_SampleType', UNIQUEIDENTIFIER),
    Column('DensityMoistureContent', DECIMAL(19, 10)),
    Column('DensityBulkDensity', DECIMAL(19, 10)),
    Column('DensityDryDensity', DECIMAL(19, 10)),
    Column('DensityRemarks', Unicode(4000)),
    Column('DensityMethod', Unicode(255)),
    Column('DensityLaboratoryName', Unicode(255)),
    Column('DensityAccreditionReference', Unicode(255)),
    Column('DensityStatus', Unicode(255)),
    Column('DensityAssociatedFileReference', Unicode(255)),
    Column('LocationDetailsId', UNIQUEIDENTIFIER, nullable=False),
    Column('SampleInformationId', UNIQUEIDENTIFIER, nullable=False),
    Column('SampleInformationstr_Type', Unicode(255)),
    Column('Densitystr_TestType', Unicode(255)),
    Column('Densitystr_SampleCondition', Unicode(255)),
    Column('Densitystr_SampleType', Unicode(255))
)


t_GridView_Dynamic_Probe_Tests___General_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'GridView_Dynamic Probe Tests - General_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('DynamicProbeGeneralId', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationDetailsLocationID', Unicode(255)),
    Column('DynamicProbeGeneralTestNumber', Unicode(255)),
    Column('DynamicProbeGeneralDateTest', DATETIME2),
    Column('DynamicProbeGeneraluui_ProbeType', UNIQUEIDENTIFIER),
    Column('DynamicProbeGeneralMethod', Unicode(255)),
    Column('DynamicProbeGeneralHammerMass', DECIMAL(19, 10)),
    Column('DynamicProbeGeneralStandardDrop', DECIMAL(19, 10)),
    Column('DynamicProbeGeneralDiameterCone', DECIMAL(19, 10)),
    Column('DynamicProbeGeneralRodDiameter', DECIMAL(19, 10)),
    Column('DynamicProbeGeneralAnvilType', Unicode(255)),
    Column('DynamicProbeGeneralAnvilDampertype', Unicode(255)),
    Column('DynamicProbeGeneralFinalConeDepth', DECIMAL(9, 3)),
    Column('DynamicProbeGeneralRemarks', Unicode(4000)),
    Column('DynamicProbeGeneralConeAngle', DECIMAL(19, 10)),
    Column('DynamicProbeGeneralRodMass', DECIMAL(19, 10)),
    Column('DynamicProbeGeneralRodFrictionPrecautions', Unicode(255)),
    Column('DynamicProbeGeneralPreDrilling', Unicode(255)),
    Column('DynamicProbeGeneralBlowCountFrequency', Unicode(255)),
    Column('DynamicProbeGeneralGroundwaterLevel', DECIMAL(19, 10)),
    Column('DynamicProbeGeneralAbortReason', Unicode(255)),
    Column('DynamicProbeGeneralWeather', Unicode(255)),
    Column('DynamicProbeGeneralOrganisationName', Unicode(255)),
    Column('DynamicProbeGeneralAccreditionReference', Unicode(255)),
    Column('DynamicProbeGeneralStatus', Unicode(255)),
    Column('DynamicProbeGeneralAssociatedFileReference', Unicode(255)),
    Column('LocationDetailsId', UNIQUEIDENTIFIER, nullable=False),
    Column('DynamicProbeGeneralstr_ProbeType', Unicode(255))
)


t_GridView_Field_Geological_Descriptions_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'GridView_Field Geological Descriptions_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('StratumDetailsId', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationDetailsLocationID', Unicode(255)),
    Column('StratumDetailsDepthTop', DECIMAL(9, 3)),
    Column('StratumDetailsDepthBase', DECIMAL(9, 3)),
    Column('StratumDetailsDescription', Unicode(4000)),
    Column('StratumDetailsuui_LegendCode', UNIQUEIDENTIFIER),
    Column('StratumDetailsuui_GeologyCode', UNIQUEIDENTIFIER),
    Column('StratumDetailsuui_GeologyCode2', UNIQUEIDENTIFIER),
    Column('StratumDetailsStratumReference', Unicode(255)),
    Column('StratumDetailsuui_BGSLexicon', UNIQUEIDENTIFIER),
    Column('StratumDetailsGeologicalformation', Unicode(255)),
    Column('StratumDetailsRemarks', Unicode(4000)),
    Column('StratumDetailsAssociatedFileReference', Unicode(255)),
    Column('LocationDetailsId', UNIQUEIDENTIFIER, nullable=False),
    Column('StratumDetailsstr_LegendCode', Unicode(255)),
    Column('StratumDetailsstr_GeologyCode', Unicode(255)),
    Column('StratumDetailsstr_GeologyCode2', Unicode(255)),
    Column('StratumDetailsstr_BGSLexicon', Unicode(255))
)


t_GridView_Laboratory_Vane_Tests_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'GridView_Laboratory Vane Tests_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LaboratoryVaneId', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationDetailsLocationID', Unicode(255)),
    Column('SampleInformationDepthTop', DECIMAL(9, 3)),
    Column('SampleInformationSampleReference', Unicode(255)),
    Column('SampleInformationuui_Type', UNIQUEIDENTIFIER),
    Column('SampleInformationSampleID', Unicode(255)),
    Column('LaboratoryVaneSpecimenReference', Unicode(255)),
    Column('LaboratoryVaneDepthSpecimenTop', DECIMAL(9, 3)),
    Column('LaboratoryVaneSpecimenDescription', Unicode(4000)),
    Column('LaboratoryVaneSpecimenPreparation', Unicode(255)),
    Column('LaboratoryVaneUndrainedShearStrengthPeak', DECIMAL(19, 10)),
    Column('LaboratoryVaneUndrainedShearStrengthRemolded', DECIMAL(19, 10)),
    Column('LaboratoryVaneMoistureContent', DECIMAL(19, 10)),
    Column('LaboratoryVaneEquivalentDiameter', DECIMAL(19, 10)),
    Column('LaboratoryVaneVaneLength', DECIMAL(19, 10)),
    Column('LaboratoryVaneRemarks', Unicode(4000)),
    Column('LaboratoryVaneMethod', Unicode(255)),
    Column('LaboratoryVaneLaboratoryName', Unicode(255)),
    Column('LaboratoryVaneAccreditionReference', Unicode(255)),
    Column('LaboratoryVaneStatus', Unicode(255)),
    Column('LaboratoryVaneAssociatedFileReference', Unicode(255)),
    Column('LaboratoryVaneuui_VaneType', UNIQUEIDENTIFIER),
    Column('LocationDetailsId', UNIQUEIDENTIFIER, nullable=False),
    Column('SampleInformationId', UNIQUEIDENTIFIER, nullable=False),
    Column('SampleInformationstr_Type', Unicode(255)),
    Column('LaboratoryVanestr_VaneType', Unicode(255))
)


t_GridView_Location_Details_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'GridView_Location Details_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetailsId', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationDetailsLocationID', Unicode(255)),
    Column('LocationDetailsuui_LocationType', UNIQUEIDENTIFIER),
    Column('LocationDetailsuui_Status', UNIQUEIDENTIFIER),
    Column('LocationDetailsEasting', DECIMAL(19, 10)),
    Column('LocationDetailsNorthing', DECIMAL(19, 10)),
    Column('LocationDetailsLatitude', Unicode(255)),
    Column('LocationDetailsLongitude', Unicode(255)),
    Column('LocationDetailsuui_NationalGridReferencingSystem', UNIQUEIDENTIFIER),
    Column('LocationDetailsGroundLevel', DECIMAL(19, 10)),
    Column('LocationDetailsRemarks', Unicode(4000)),
    Column('LocationDetailsuui_WellCapType', UNIQUEIDENTIFIER),
    Column('LocationDetailsFinalDepth', DECIMAL(9, 3)),
    Column('LocationDetailsDateStart', DATETIME2),
    Column('LocationDetailsLocationPurpose', Unicode(255)),
    Column('LocationDetailsTerminationReason', Unicode(255)),
    Column('LocationDetailsDateEnd', DATETIME2),
    Column('LocationDetailsGridLetterReference', Unicode(255)),
    Column('LocationDetailsLocalXGrid', DECIMAL(19, 10)),
    Column('LocationDetailsLocalYGrid', DECIMAL(19, 10)),
    Column('LocationDetailsLocalLevel', DECIMAL(19, 10)),
    Column('LocationDetailsLocalDatum', Unicode(255)),
    Column('LocationDetailsLocalGridSystem', Unicode(255)),
    Column('LocationDetailsEastingTraverseEnd', DECIMAL(19, 10)),
    Column('LocationDetailsNorthingTraverseEnd', DECIMAL(19, 10)),
    Column('LocationDetailsGroundLevelEnd', DECIMAL(19, 10)),
    Column('LocationDetailsLocalXEnd', DECIMAL(19, 10)),
    Column('LocationDetailsLocalYEnd', DECIMAL(19, 10)),
    Column('LocationDetailsLocalLevelEnd', DECIMAL(19, 10)),
    Column('LocationDetailsLatitudeEnd', Unicode(255)),
    Column('LocationDetailsLongitudeEnd', Unicode(255)),
    Column('LocationDetailsProjectionFormat', Unicode(255)),
    Column('LocationDetailsLocationingMethod', Unicode(255)),
    Column('LocationDetailsSubLocation', Unicode(255)),
    Column('LocationDetailsPhase', Unicode(255)),
    Column('LocationDetailsAlignmentID', Unicode(255)),
    Column('LocationDetailsOffset', DECIMAL(19, 10)),
    Column('LocationDetailsChainage', Unicode(255)),
    Column('LocationDetailsTransformation', Unicode(255)),
    Column('LocationDetailsAssociatedFileReference', Unicode(255)),
    Column('LocationDetailsCheckedBy', Unicode(255)),
    Column('LocationDetailsApprovedBy', Unicode(255)),
    Column('LocationDetailsId_2', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationDetailsstr_LocationType', Unicode(255)),
    Column('LocationDetailsstr_Status', Unicode(255)),
    Column('LocationDetailsstr_NationalGridReferencingSystem', Unicode(255)),
    Column('LocationDetailsstr_WellCapType', Unicode(255))
)


t_GridView_Monitoring_Installations_and_Instruments_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'GridView_Monitoring Installations and Instruments_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('MonitoringInstallationsAndInstrumentsId', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationDetailsLocationID', Unicode(255)),
    Column('MonitoringInstallationsAndInstrumentsPointReference', Unicode(255)),
    Column('MonitoringInstallationsAndInstrumentsDistance', DECIMAL(19, 10)),
    Column('MonitoringInstallationsAndInstrumentsPipeReference', Unicode(255)),
    Column('MonitoringInstallationsAndInstrumentsDateInstallation', DATETIME2),
    Column('MonitoringInstallationsAndInstrumentsuui_InstrumentType', UNIQUEIDENTIFIER),
    Column('MonitoringInstallationsAndInstrumentsPipeHeight', DECIMAL(19, 10)),
    Column('MonitoringInstallationsAndInstrumentsPipeElevation', DECIMAL(19, 10)),
    Column('MonitoringInstallationsAndInstrumentsuui_PipeCoverType', UNIQUEIDENTIFIER),
    Column('MonitoringInstallationsAndInstrumentsInstrumentDetails', Unicode(4000)),
    Column('MonitoringInstallationsAndInstrumentsDepthResponseZoneTop', DECIMAL(9, 3)),
    Column('MonitoringInstallationsAndInstrumentsDepthResponseZoneBase', DECIMAL(9, 3)),
    Column('MonitoringInstallationsAndInstrumentsBearingA', DECIMAL(19, 10)),
    Column('MonitoringInstallationsAndInstrumentsBearingB', DECIMAL(19, 10)),
    Column('MonitoringInstallationsAndInstrumentsBearingC', DECIMAL(19, 10)),
    Column('MonitoringInstallationsAndInstrumentsInclinationA', DECIMAL(19, 10)),
    Column('MonitoringInstallationsAndInstrumentsInclinationB', DECIMAL(19, 10)),
    Column('MonitoringInstallationsAndInstrumentsInclinationC', DECIMAL(19, 10)),
    Column('MonitoringInstallationsAndInstrumentsSignConventionA', Unicode(255)),
    Column('MonitoringInstallationsAndInstrumentsSignConventionB', Unicode(255)),
    Column('MonitoringInstallationsAndInstrumentsSignConventionC', Unicode(255)),
    Column('MonitoringInstallationsAndInstrumentsRemarks', Unicode(4000)),
    Column('MonitoringInstallationsAndInstrumentsContractor', Unicode(255)),
    Column('MonitoringInstallationsAndInstrumentsAssociatedFileReference', Unicode(255)),
    Column('LocationDetailsId', UNIQUEIDENTIFIER, nullable=False),
    Column('MonitoringInstallationsAndInstrumentsstr_InstrumentType', Unicode(255)),
    Column('MonitoringInstallationsAndInstrumentsstr_PipeCoverType', Unicode(255))
)


t_GridView_Particle_Size_Distribution_Analysis___Data_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'GridView_Particle Size Distribution Analysis - Data_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('ParticleSizeDistributionDataId', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationDetailsLocationID', Unicode(255)),
    Column('SampleInformationDepthTop', DECIMAL(9, 3)),
    Column('SampleInformationSampleReference', Unicode(255)),
    Column('SampleInformationuui_Type', UNIQUEIDENTIFIER),
    Column('SampleInformationSampleID', Unicode(255)),
    Column('ParticleSizeDistributionGeneralSpecimenReference', Unicode(255)),
    Column('ParticleSizeDistributionGeneralDepthSpecimenTop', DECIMAL(9, 3)),
    Column('ParticleSizeDistributionDataParticleSize', DECIMAL(19, 10)),
    Column('ParticleSizeDistributionDataPercentagePassing', DECIMAL(19, 10)),
    Column('ParticleSizeDistributionDatauui_TestType', UNIQUEIDENTIFIER),
    Column('ParticleSizeDistributionDataRemarks', Unicode(4000)),
    Column('ParticleSizeDistributionDataAssociatedFileReference', Unicode(255)),
    Column('LocationDetailsId', UNIQUEIDENTIFIER, nullable=False),
    Column('SampleInformationId', UNIQUEIDENTIFIER, nullable=False),
    Column('ParticleSizeDistributionGeneralId', UNIQUEIDENTIFIER, nullable=False),
    Column('SampleInformationstr_Type', Unicode(255)),
    Column('ParticleSizeDistributionDatastr_TestType', Unicode(255))
)


t_GridView_Particle_Size_Distribution_Analysis___General_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'GridView_Particle Size Distribution Analysis - General_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('ParticleSizeDistributionGeneralId', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationDetailsLocationID', Unicode(255)),
    Column('SampleInformationDepthTop', DECIMAL(9, 3)),
    Column('SampleInformationSampleReference', Unicode(255)),
    Column('SampleInformationuui_Type', UNIQUEIDENTIFIER),
    Column('SampleInformationSampleID', Unicode(255)),
    Column('ParticleSizeDistributionGeneralSpecimenReference', Unicode(255)),
    Column('ParticleSizeDistributionGeneralDepthSpecimenTop', DECIMAL(9, 3)),
    Column('ParticleSizeDistributionGeneralSpecimenDescription', Unicode(4000)),
    Column('ParticleSizeDistributionGeneralSpecimenPreparation', Unicode(255)),
    Column('ParticleSizeDistributionGeneralUniformityCoefficient', DECIMAL(19, 10)),
    Column('ParticleSizeDistributionGeneralPercentageCobbles', DECIMAL(19, 10)),
    Column('ParticleSizeDistributionGeneralPercentageGravel', DECIMAL(19, 10)),
    Column('ParticleSizeDistributionGeneralPercentageSand', DECIMAL(19, 10)),
    Column('ParticleSizeDistributionGeneralPercentageSilt', DECIMAL(19, 10)),
    Column('ParticleSizeDistributionGeneralPercentageClay', DECIMAL(19, 10)),
    Column('ParticleSizeDistributionGeneralPercentageFines', DECIMAL(19, 10)),
    Column('ParticleSizeDistributionGeneralRemarks', Unicode(4000)),
    Column('ParticleSizeDistributionGeneralMethod', Unicode(255)),
    Column('ParticleSizeDistributionGeneralLaboratoryName', Unicode(255)),
    Column('ParticleSizeDistributionGeneralAccreditionReference', Unicode(255)),
    Column('ParticleSizeDistributionGeneralStatus', Unicode(255)),
    Column('ParticleSizeDistributionGeneralAssociatedFileReference', Unicode(255)),
    Column('LocationDetailsId', UNIQUEIDENTIFIER, nullable=False),
    Column('SampleInformationId', UNIQUEIDENTIFIER, nullable=False),
    Column('SampleInformationstr_Type', Unicode(255))
)


t_GridView_Sample_Information_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'GridView_Sample Information_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('SampleInformationId', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationDetailsLocationID', Unicode(255)),
    Column('SampleInformationDepthTop', DECIMAL(9, 3)),
    Column('SampleInformationSampleReference', Unicode(255)),
    Column('SampleInformationuui_Type', UNIQUEIDENTIFIER),
    Column('SampleInformationSampleID', Unicode(255)),
    Column('SampleInformationDepthBase', DECIMAL(9, 3)),
    Column('SampleInformationDateTimeSampled', DATETIME2),
    Column('SampleInformationBlows', DECIMAL(19, 10)),
    Column('SampleInformationSampleContainer', Unicode(255)),
    Column('SampleInformationPreparation', Unicode(255)),
    Column('SampleInformationDiameter', DECIMAL(19, 10)),
    Column('SampleInformationWaterDepth', Unicode(50)),
    Column('SampleInformationRecovery', DECIMAL(19, 10)),
    Column('SampleInformationMethod', Unicode(255)),
    Column('SampleInformationMatrix', Unicode(255)),
    Column('SampleInformationQAType', Unicode(255)),
    Column('SampleInformationSampler', Unicode(255)),
    Column('SampleInformationReason', Unicode(255)),
    Column('SampleInformationRemarks', Unicode(4000)),
    Column('SampleInformationDescription', Unicode(4000)),
    Column('SampleInformationDateDescribed', DATETIME2),
    Column('SampleInformationDescriptionBy', Unicode(4000)),
    Column('SampleInformationSpecimenCondition', Unicode(255)),
    Column('SampleInformationClassification', Unicode(255)),
    Column('SampleInformationBarometricPressure', DECIMAL(19, 10)),
    Column('SampleInformationTemperature', DECIMAL(19, 10)),
    Column('SampleInformationGasPressure', DECIMAL(19, 10)),
    Column('SampleInformationGasFlowRate', DECIMAL(19, 10)),
    Column('SampleInformationDateTimeCompleted', DATETIME2),
    Column('SampleInformationDuration', BigInteger),
    Column('SampleInformationCaption', Unicode(255)),
    Column('SampleInformationSampleRecordLink', Unicode(255)),
    Column('SampleInformationStratumReference', Unicode(255)),
    Column('SampleInformationAssociatedFileReference', Unicode(255)),
    Column('LocationDetailsId', UNIQUEIDENTIFIER, nullable=False),
    Column('SampleInformationstr_Type', Unicode(255))
)


t_GridView_Static_Cone_Penetration_Tests___Data_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'GridView_Static Cone Penetration Tests - Data_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('StaticConePenetrationDataId', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationDetailsLocationID', Unicode(255)),
    Column('StaticConePenetrationGeneralTestNumber', Unicode(255)),
    Column('StaticConePenetrationDataDepth', DECIMAL(9, 3)),
    Column('StaticConePenetrationDataConeResistance', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataLocalUnitSideFrictionResistance', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataFacePorewaterPressure', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataShoulderPorewaterPressure', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataTopOfSleevePorewaterPressure', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataConductivity', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataTemperature', DECIMAL(19, 10)),
    Column('StaticConePenetrationDatapH', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataSlopeIndicator1', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataSlopeIndicator2', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataRedoxPotential', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataMagneticFluxTotal', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataMagneticFluxX', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataMagneticFluxY', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataMagneticFluxZ', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataSoilMoisture', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataNaturalGammaRadiation', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataRemarks', Unicode(4000)),
    Column('StaticConePenetrationDataFrictionRatio', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataCorrectedConeResistance', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataCorrectedSleeveResistance', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataEffectiveConeResistance', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataBulkDensity', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataTotalVerticalStress', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataEffectiveverticalstress', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataNetConeResistance', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataCorrectedFrictionRatio', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataExcessPorePressure', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataPorePressureRatio', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataInSituPorePressure', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataNormalisedConeResistance', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataNormalisedFrictionRatio', DECIMAL(19, 10)),
    Column('StaticConePenetrationDataFID', DECIMAL(12, 3)),
    Column('StaticConePenetrationDataPID', DECIMAL(12, 3)),
    Column('StaticConePenetrationDataFI', DECIMAL(12, 3)),
    Column('StaticConePenetrationDataPhtotoMultiplier', Integer),
    Column('StaticConePenetrationDataAssociatedFileReference', Unicode(255)),
    Column('LocationDetailsId', UNIQUEIDENTIFIER, nullable=False),
    Column('StaticConePenetrationGeneralId', UNIQUEIDENTIFIER, nullable=False)
)


t_GridView_Users_00000000_0000_0000_0000_000000000000 = Table(
    'GridView_Users_00000000_0000_0000_0000_000000000000', metadata,
    Column('AuthUserId', UNIQUEIDENTIFIER, nullable=False),
    Column('AuthUserWindowsAuthentication', BIT),
    Column('AuthUserUsername', Unicode(255)),
    Column('AuthUseruui_Title', UNIQUEIDENTIFIER),
    Column('AuthUserFirstName', Unicode(255)),
    Column('AuthUserSurname', Unicode(255)),
    Column('AuthUserEmail', Unicode(255)),
    Column('AuthUserLandlineNumber', Unicode(255)),
    Column('AuthUserMobileNumber', Unicode(255)),
    Column('AuthUserIsActive', BIT),
    Column('AuthUserIsExternal', BIT),
    Column('AuthUserExpiryDate', DateTime),
    Column('AuthUserIsSysAdmin', BIT),
    Column('AuthUserId_2', UNIQUEIDENTIFIER, nullable=False),
    Column('AuthUserstr_Title', Unicode(255))
)


class SYSAbout(Base):
    __tablename__ = 'SYS_About'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    Key = Column(Unicode(255))
    Value = Column(Unicode(255))


class SYSAuditLog(Base):
    __tablename__ = 'SYS_AuditLog'
    __table_args__ = (
        Index('IX_SYS_AuditLog_ProjectEntityNameDate', 'Project', 'EntityName', 'Date'),
        Index('IX_SYS_AuditLog_EntityDate', 'EntityName', 'Date')
    )

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Entity = Column(UNIQUEIDENTIFIER, index=True)
    EntityName = Column(Unicode(255), index=True)
    Action = Column(Unicode(50))
    ActionDescription = Column(Unicode(50))
    Date = Column(DateTime, index=True)
    user = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class SYSAuthGroup(Base):
    __tablename__ = 'SYS_AuthGroup'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255))
    Description = Column(Unicode(255))
    IsSystemLevel = Column(BIT)


class SYSAuthGroupRole(Base):
    __tablename__ = 'SYS_AuthGroupRole'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    AuthGroup = Column(UNIQUEIDENTIFIER, index=True)
    AuthRole = Column(UNIQUEIDENTIFIER, index=True)


class SYSAuthUserGroup(Base):
    __tablename__ = 'SYS_AuthUserGroup'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    AuthUser = Column(UNIQUEIDENTIFIER, index=True)
    AuthGroup = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ProjectIsCurrent = Column(BIT)


class SYSCache(Base):
    __tablename__ = 'SYS_Cache'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Type = Column(Unicode(255), index=True)
    DateCached = Column(DATETIME2)
    Key = Column(UNIQUEIDENTIFIER, index=True)
    Data = Column(LargeBinary)
    DependencyKey = Column(UNIQUEIDENTIFIER)
    Version = Column(Unicode(255), index=True)


class SYSCacheDataCount(Base):
    __tablename__ = 'SYS_CacheDataCount'
    __table_args__ = (
        Index('IX_SYS_CacheDataCount_Project_Entityname_DateCached', 'Project', 'Entityname', 'DateCached'),
    )

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Entityname = Column(Unicode(255))
    Project = Column(UNIQUEIDENTIFIER)
    DateCached = Column(DATETIME2)
    Count = Column(Integer)


t_SYS_Compatibility = Table(
    'SYS_Compatibility', metadata,
    Column('Id', UNIQUEIDENTIFIER, nullable=False),
    Column('Product', Unicode(255)),
    Column('Version', BigInteger)
)


class SYSComponentImportHistory(Base):
    __tablename__ = 'SYS_ComponentImportHistory'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    FileName = Column(Unicode(255))
    ImportType = Column(Unicode(50))


class SYSDocument(Base):
    __tablename__ = 'SYS_Document'
    __table_args__ = (
        Index('IX_SYS_Document_NameType', 'Name', 'Type'),
    )

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255))
    Description = Column(Unicode(4000))
    FileName = Column(Unicode(255))
    Extension = Column(Unicode(255))
    Type = Column(Unicode(255))
    FileSize = Column(BigInteger)
    Version = Column(Integer)
    IsActive = Column(BIT)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    ParentVersionId = Column(UNIQUEIDENTIFIER)
    Properties = Column(Unicode(4000))


class SYSDocumentExtension(Base):
    __tablename__ = 'SYS_DocumentExtension'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255))
    Extension = Column(Unicode(255))
    FileSize = Column(BigInteger)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class SYSDocumentMetaDatum(Base):
    __tablename__ = 'SYS_DocumentMetaData'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    ParentProgram = Column(Unicode(255))
    FileFSETReference = Column(Unicode(255))
    Secured = Column(BIT)
    IncludeInAGSExport = Column(BIT)
    UserUploaded = Column(UNIQUEIDENTIFIER)
    DateUploaded = Column(DATETIME2)
    Category = Column(UNIQUEIDENTIFIER, index=True)
    Status = Column(UNIQUEIDENTIFIER, index=True)
    ReportOutput = Column(BIT)


class SYSDocumentObjectLink(Base):
    __tablename__ = 'SYS_DocumentObjectLink'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    EntityName = Column(Unicode(255), index=True)
    ObjectId = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Document = Column(UNIQUEIDENTIFIER, index=True)


class SYSDocumentPropertyLink(Base):
    __tablename__ = 'SYS_DocumentPropertyLink'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    EntityName = Column(Unicode(255), index=True)
    PropertyName = Column(Unicode(255), index=True)
    Value = Column(Unicode(4000), index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    ConfigPack = Column(UNIQUEIDENTIFIER, index=True)
    Document = Column(UNIQUEIDENTIFIER, index=True)


class SYSExportLogEntry(Base):
    __tablename__ = 'SYS_ExportLogEntry'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    Producer = Column(Unicode(4000))
    Recipient = Column(Unicode(4000))
    Description = Column(Unicode(4000))
    Status = Column(Unicode(4000))
    InternalCounter = Column(Integer)
    ExternalCounter = Column(Integer)


class SYSImportEntry(Base):
    __tablename__ = 'SYS_ImportEntry'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    User = Column(UNIQUEIDENTIFIER)
    Timestamp = Column(DateTime)
    Comment = Column(Unicode(4000))
    Status = Column(Unicode(255))
    Project = Column(UNIQUEIDENTIFIER)
    FileCount = Column(Integer)
    Compressed = Column(BIT, nullable=False, server_default=text("((0))"))
    Format = Column(Unicode(255))
    ImportTaskOptions = Column(Unicode(4000))
    UploadTime = Column(DateTime)
    UploadUser = Column(UNIQUEIDENTIFIER)
    ImportTime = Column(DateTime)
    ImportUser = Column(UNIQUEIDENTIFIER)
    Origin = Column(Unicode(255))


class SYSImportLock(Base):
    __tablename__ = 'SYS_ImportLock'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    User = Column(UNIQUEIDENTIFIER)


class SYSMapDatasetIndex(Base):
    __tablename__ = 'SYS_MapDatasetIndex'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    Type = Column(Unicode(255), nullable=False)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)
    Description = Column(Unicode(4000))
    Name = Column(Unicode(4000))
    TableName = Column(Unicode(4000))
    MapCoordinateSystem = Column(UNIQUEIDENTIFIER)


class SYSProjectUser(Base):
    __tablename__ = 'SYS_ProjectUser'
    __table_args__ = (
        Index('IX_SYS_ProjectUser_Project', 'Project', 'User'),
    )

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    User = Column(UNIQUEIDENTIFIER)
    Current = Column(BIT)


class SYSSectionLine(Base):
    __tablename__ = 'SYS_SectionLine'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Name = Column(Unicode(255))
    Source = Column(Unicode(255))
    Geometry = Column(NullType)
    Project = Column(UNIQUEIDENTIFIER)
    ConfigPack = Column(UNIQUEIDENTIFIER)
    Buffer = Column(DECIMAL(10, 2))
    Chainage = Column(DECIMAL(10, 2))
    Colour = Column(Integer)
    Direction = Column(BIT)


class SYSSnapshot(Base):
    __tablename__ = 'SYS_Snapshot'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Comment = Column(Unicode(4000))
    DateTaken = Column(DateTime)
    Type = Column(Unicode(255), nullable=False)
    Current = Column(BIT)
    uui_parent = Column(UNIQUEIDENTIFIER)
    AutoGenerated = Column(BIT)
    User = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER, index=True)


class SYSTask(Base):
    __tablename__ = 'SYS_Task'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Project = Column(UNIQUEIDENTIFIER)
    Created = Column(DateTime)
    Started = Column(DateTime)
    Completed = Column(DateTime)
    Status = Column(Unicode(255))
    User = Column(UNIQUEIDENTIFIER)
    Type = Column(Unicode(4000))
    Options = Column(LargeBinary(8000))
    Results = Column(LargeBinary(8000))
    Progress = Column(Integer)


class SYSTemporary(Base):
    __tablename__ = 'SYS_Temporary'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newsequentialid())"))
    Key = Column(UNIQUEIDENTIFIER, index=True)
    Session = Column(UNIQUEIDENTIFIER, index=True)
    sysDate = Column(DateTime, index=True, server_default=text("(getdate())"))


class SYSTemporaryDocument(Base):
    __tablename__ = 'SYS_TemporaryDocument'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    Name = Column(Unicode(255), nullable=False)
    Created = Column(DateTime, nullable=False)
    Length = Column(BigInteger, nullable=False)
    User = Column(UNIQUEIDENTIFIER, nullable=False)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime)
    sysAction = Column(Unicode(255))
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)


class SYSTransaction(Base):
    __tablename__ = 'SYS_Transaction'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    DateTime = Column(DateTime)
    User = Column(UNIQUEIDENTIFIER, nullable=False)


class SYSUpgradeHistory(Base):
    __tablename__ = 'SYS_UpgradeHistory'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER)
    Script = Column(Unicode(255))
    DateExecuted = Column(DateTime)
    TargetVersionNum = Column(BigInteger)
    ConfigPack = Column(UNIQUEIDENTIFIER)


t_VIEW_AuditProject = Table(
    'VIEW_AuditProject', metadata,
    Column('count', Integer),
    Column('EntityName', Unicode(255)),
    Column('Action', Unicode(50)),
    Column('Username', Unicode(255)),
    Column('date', SMALLDATETIME),
    Column('ProjectID', Unicode(50)),
    Column('Project', UNIQUEIDENTIFIER),
    Column('ActionDescription', Unicode(50))
)


t_VIEW_Backfill_to_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Backfill_to_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Location ID', Unicode(255)),
    Column('Final Depth', DECIMAL(9, 3)),
    Column('Max Base Depth', DECIMAL(9, 3))
)


t_VIEW_COC_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_COC_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('COC Reference', Unicode(255)),
    Column('COC Batch No', Unicode(255)),
    Column('COC Date Dispatch', DATETIME2),
    Column('COC No Containers', DECIMAL(19, 10)),
    Column('COC Samples From', Unicode(255)),
    Column('COC Samples To', Unicode(255)),
    Column('COC Remarks', Unicode(4000)),
    Column('LocationID', Unicode(255)),
    Column('Sample ID', Unicode(255)),
    Column('Sample Reference', Unicode(255)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Depth Top', DECIMAL(9, 3)),
    Column('Sample Depth Base', DECIMAL(9, 3)),
    Column('Sample Remarks', Unicode(4000))
)


t_VIEW_CPT_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_CPT_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationID', Unicode(255)),
    Column('GeologyCode', Unicode(255)),
    Column('GeologyCodeDescription', Unicode(4000)),
    Column('GeologyDescription', Unicode(4000)),
    Column('GeologyCode2', Unicode(255)),
    Column('GeologyCode2Description', Unicode(4000)),
    Column('LegendCode', Unicode(255)),
    Column('LegendCodeDescription', Unicode(4000)),
    Column('GeologyFormation', Unicode(255)),
    Column('BGSLexicon', Unicode(255)),
    Column('BGSLexiconDescription', Unicode(4000)),
    Column('ConeReference', Unicode(255)),
    Column('TestNumber', Unicode(255)),
    Column('Value', Unicode(255)),
    Column('ConeAreaRatio', DECIMAL(19, 10)),
    Column('DepthGroundwater', DECIMAL(9, 3)),
    Column('DepthWaterOriginal', Unicode(255)),
    Column('FilterMaterial', Unicode(255)),
    Column('FrictionReducerUsed', BIT),
    Column('Method', Unicode(255)),
    Column('NominalRateOfPenetration', DECIMAL(19, 10)),
    Column('GeneralRemarks', Unicode(4000)),
    Column('SleeveAreaRatio', DECIMAL(19, 10)),
    Column('SurfaceArea', DECIMAL(19, 10)),
    Column('Weather', Unicode(255)),
    Column('Depth', DECIMAL(9, 3)),
    Column('BulkDensity', DECIMAL(19, 10)),
    Column('Conductivity', DECIMAL(19, 10)),
    Column('ConeResistance', DECIMAL(19, 10)),
    Column('CorrectedConeResistance', DECIMAL(19, 10)),
    Column('CorrectedFrictionratio', DECIMAL(19, 10)),
    Column('CorrectedSleeveResistance', DECIMAL(19, 10)),
    Column('EffectiveConeResistance', DECIMAL(19, 10)),
    Column('Effectiveverticalstress', DECIMAL(19, 10)),
    Column('ExcessPorePressure', DECIMAL(19, 10)),
    Column('FacePorewaterPressure', DECIMAL(19, 10)),
    Column('FrictionRatio', DECIMAL(19, 10)),
    Column('InSituPorePressure', DECIMAL(19, 10)),
    Column('LocalUnitSideFrictionResistance', DECIMAL(19, 10)),
    Column('MagneticFluxTotal', DECIMAL(19, 10)),
    Column('MagneticFluxX', DECIMAL(19, 10)),
    Column('MagneticFluxY', DECIMAL(19, 10)),
    Column('MagneticFluxZ', DECIMAL(19, 10)),
    Column('NaturalGammaRadiation', DECIMAL(19, 10)),
    Column('NetConeResistance', DECIMAL(19, 10)),
    Column('NormalisedConeResistance', DECIMAL(19, 10)),
    Column('NormalisedFrictionRatio', DECIMAL(19, 10)),
    Column('PH', DECIMAL(19, 10)),
    Column('PorePressureRatio', DECIMAL(19, 10)),
    Column('RedoxPotential', DECIMAL(19, 10)),
    Column('DataRemarks', Unicode(4000)),
    Column('ShoulderPorewaterPressure', DECIMAL(19, 10)),
    Column('SlopeIndicator1', DECIMAL(19, 10)),
    Column('SlopeIndicator2', DECIMAL(19, 10)),
    Column('SoilMoisture', DECIMAL(19, 10)),
    Column('Temperature', DECIMAL(19, 10)),
    Column('TopOfSleevePorewaterPressure', DECIMAL(19, 10)),
    Column('TotalVerticalStress', DECIMAL(19, 10)),
    Column('FI', DECIMAL(12, 3)),
    Column('FID', DECIMAL(12, 3)),
    Column('PhtotoMultiplier', Integer),
    Column('PID', DECIMAL(12, 3)),
    Column('DepthTop', DECIMAL(9, 3)),
    Column('DepthBase', DECIMAL(9, 3)),
    Column('EquivalentSPTN60', DECIMAL(19, 10)),
    Column('InternalFrictionAngle', DECIMAL(19, 10)),
    Column('Interpretationreference', Unicode(255)),
    Column('InterpretedSoilType', Unicode(255)),
    Column('RelativeDensity', DECIMAL(19, 10)),
    Column('ParameterRemarks', Unicode(4000)),
    Column('SoilBehaviourTypeIndex', DECIMAL(19, 10)),
    Column('UndrainedShearStrength', DECIMAL(19, 10))
)


t_VIEW_Chiselling_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Chiselling_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code 2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geology Description', Unicode(4000)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Depth Top', DECIMAL(9, 3)),
    Column('Depth Base', DECIMAL(9, 3)),
    Column('Duration', BigInteger),
    Column('Time Start', DATETIME2),
    Column('Tool', Unicode(255))
)


t_VIEW_Classification_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Classification_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geology Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Top Depth', DECIMAL(9, 3)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Reference', Unicode(255)),
    Column('SampleID', Unicode(255)),
    Column('Base Depth', DECIMAL(9, 3)),
    Column('MC Specimen Depth', DECIMAL(9, 3)),
    Column('MC Specimen Reference', Unicode(255)),
    Column('MC Specimen Description', Unicode(4000)),
    Column('MC Specimen Preparation', Unicode(255)),
    Column('Moisture Content', DECIMAL(19, 10)),
    Column('Is Natural MC', BIT),
    Column('LLPL Specimen Depth', DECIMAL(9, 3)),
    Column('LLPL Specimen Reference', Unicode(255)),
    Column('LLPL Specimen Description', Unicode(4000)),
    Column('LLPL Specimen Preparation', Unicode(255)),
    Column('Liquid Limit', DECIMAL(19, 10)),
    Column('Plasticity Index', DECIMAL(19, 10)),
    Column('Plastic Limit', Unicode(255)),
    Column('Plastic Limit Value', DECIMAL(19, 10)),
    Column('Limit Percentage Passing', DECIMAL(19, 10)),
    Column('Limit Size Passing', DECIMAL(19, 10)),
    Column('Limit Remarks', Unicode(4000)),
    Column('Limit Method', Unicode(255)),
    Column('Grading Specimen Depth', DECIMAL(9, 3)),
    Column('Grading Specimen Reference', Unicode(255)),
    Column('Grading Specimen Description', Unicode(4000)),
    Column('Grading Specimen Preparation', Unicode(255)),
    Column('Uniformity Coefficient', DECIMAL(19, 10)),
    Column('Clay Percentage', DECIMAL(19, 10)),
    Column('Silt Percentage', DECIMAL(19, 10)),
    Column('Sand Percentage', DECIMAL(19, 10)),
    Column('Gravel Percentage', DECIMAL(19, 10)),
    Column('Cobbles Percentage', DECIMAL(19, 10)),
    Column('Fines Percentage', DECIMAL(19, 10)),
    Column('PD Specimen Depth', DECIMAL(9, 3)),
    Column('PD Specimen Reference', Unicode(255)),
    Column('PD Specimen Description', Unicode(4000)),
    Column('PD Specimen Preparation', Unicode(255)),
    Column('Particle Density', DECIMAL(19, 10)),
    Column('Particle Density Method', Unicode(255)),
    Column('Shrinkage Specimen Depth', DECIMAL(9, 3)),
    Column('Shrinkage Specimen Reference', Unicode(255)),
    Column('Shrinkage Specimen Description', Unicode(4000)),
    Column('Shrinkage Specimen Preparation', Unicode(255)),
    Column('Shrinkage Limit', DECIMAL(19, 10)),
    Column('Shrinkage Ratio', DECIMAL(19, 10)),
    Column('Density Specimen Top', DECIMAL(9, 3)),
    Column('Density Specimen Reference', Unicode(255)),
    Column('Density Specimen Description', Unicode(4000)),
    Column('Density Specimen Preparation', Unicode(255)),
    Column('Density Test Type', Unicode(255)),
    Column('Bulk Density', DECIMAL(19, 10)),
    Column('Dry Density', DECIMAL(19, 10)),
    Column('Density Moisture Content', DECIMAL(19, 10)),
    Column('Organic Content', Unicode(50)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3))
)


t_VIEW_Compaction_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Compaction_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geology Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Top Depth', DECIMAL(9, 3)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Reference', Unicode(255)),
    Column('Base Depth', DECIMAL(9, 3)),
    Column('Test Number', Unicode(255)),
    Column('Sample Description', Unicode(4000)),
    Column('Specimen Depth', DECIMAL(9, 3)),
    Column('Specimen Reference', Unicode(255)),
    Column('Specimen Description', Unicode(4000)),
    Column('Specimen Preparation', Unicode(255)),
    Column('Max Dry Density', DECIMAL(19, 10)),
    Column('Optimum Moisture Content', DECIMAL(19, 10)),
    Column('Particle Density', DECIMAL(19, 10)),
    Column('PD Method', Unicode(255)),
    Column('Method', Unicode(255)),
    Column('Test Type', Unicode(255)),
    Column('Mould Type', Unicode(255)),
    Column('Remarks', Unicode(4000)),
    Column('Percentage Passing Size 1', DECIMAL(19, 10)),
    Column('Size 1', DECIMAL(19, 10)),
    Column('Percentage Passing Size 2', DECIMAL(19, 10)),
    Column('Size 2', DECIMAL(19, 10)),
    Column('Stabiliser Amount', DECIMAL(19, 10)),
    Column('Stabiliser Type', Unicode(255)),
    Column('Status', Unicode(255)),
    Column('Point Number', Unicode(255)),
    Column('Maximum Dry Density', DECIMAL(19, 10)),
    Column('Moisture Content', DECIMAL(19, 10)),
    Column('Test Remarks', Unicode(4000)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3))
)


t_VIEW_Consolidation_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Consolidation_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Top Depth', DECIMAL(9, 3)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Reference', Unicode(255)),
    Column('Base Depth', DECIMAL(9, 3)),
    Column('Test Type', Unicode(255)),
    Column('Initial Bulk Density', DECIMAL(19, 10)),
    Column('Stress Range', Unicode(255)),
    Column('Initial Degree of Saturation', DECIMAL(19, 10)),
    Column('Specimen Top', DECIMAL(9, 3)),
    Column('Specimen Reference', Unicode(255)),
    Column('Specimen Description', Unicode(4000)),
    Column('Specimen Preparation', Unicode(255)),
    Column('Specimen Height', DECIMAL(19, 10)),
    Column('Initial Dry Density', DECIMAL(19, 10)),
    Column('Particle Density Method', Unicode(255)),
    Column('Sample Condition', Unicode(255)),
    Column('Diameter', DECIMAL(19, 10)),
    Column('Final MC', DECIMAL(19, 10)),
    Column('Initial MC', DECIMAL(19, 10)),
    Column('Particle Density', DECIMAL(19, 10)),
    Column('Initial Voids Ratio', DECIMAL(19, 10)),
    Column('Saturation Height Change', DECIMAL(19, 10)),
    Column('General Volume Compressibility', DECIMAL(19, 10)),
    Column('Increment No', Unicode(255)),
    Column('Coefficient of Consolidation Log Time', DECIMAL(19, 10)),
    Column('Coefficient of consolidation Root Time', DECIMAL(19, 10)),
    Column('Volume Compressibility Coefficient', DECIMAL(19, 10)),
    Column('Reported Coefficient of Consolidation', DECIMAL(19, 10)),
    Column('Secondary Compression Coefficient', DECIMAL(19, 10)),
    Column('Stress at Stage End', DECIMAL(19, 10)),
    Column('Average Temperature', DECIMAL(19, 10)),
    Column('Start Voids Ratio', DECIMAL(19, 10)),
    Column('End Voids Ratio', DECIMAL(19, 10)),
    Column('Test Remarks', Unicode(4000)),
    Column('Swelling Presure', DECIMAL(19, 10)),
    Column('General Remarks', Unicode(4000)),
    Column('Method', Unicode(255)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3))
)


t_VIEW_Contaminate_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Contaminate_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Top Depth', DECIMAL(9, 3)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Reference', Unicode(255)),
    Column('Base Depth', DECIMAL(9, 3)),
    Column('Specimen Top', DECIMAL(9, 3)),
    Column('Specimen Reference', Unicode(255)),
    Column('Specimen Description', Unicode(4000)),
    Column('Specimen Preparation', Unicode(255)),
    Column('Determinand', Unicode(255)),
    Column('Determinand Description', Unicode(4000)),
    Column('Test Type', Unicode(255)),
    Column('Test Type Description', Unicode(4000)),
    Column('Chemical Code', Unicode(255)),
    Column('Chemical Code Description', Unicode(4000)),
    Column('Chemical Name', Unicode(255)),
    Column('Total Or Dissolved', Unicode(255)),
    Column('Reported Result', Unicode(255)),
    Column('Result Value', DECIMAL(19, 10)),
    Column('Result Unit', Unicode(255)),
    Column('Laboratory Test Matrix', Unicode(255)),
    Column('Laboratory Test Matrix Description', Unicode(4000)),
    Column('Date Received', DATETIME2),
    Column('Date Leachate Preparation', DATETIME2),
    Column('Date Time Tested', DATETIME2),
    Column('Basis', Unicode(255)),
    Column('Basis Description', Unicode(4000)),
    Column('Method', Unicode(255)),
    Column('Method Detection Limit', DECIMAL(19, 10)),
    Column('Unit of Detection', Unicode(255)),
    Column('Reporting Detection Limit', DECIMAL(19, 10)),
    Column('Reportable Result', BIT),
    Column('Quantification Limit', DECIMAL(19, 10)),
    Column('Result Type', Unicode(255)),
    Column('Result Type Description', Unicode(4000)),
    Column('Run Type', Unicode(255)),
    Column('Run Type Description', Unicode(4000)),
    Column('Batch Code', Unicode(255)),
    Column('Dilution Factor', DECIMAL(19, 10)),
    Column('Instrument Reference', Unicode(255)),
    Column('Interpreted Qualifiers', Unicode(255)),
    Column('Detected', BIT),
    Column('Organic', BIT),
    Column('Laboratory Name', Unicode(255)),
    Column('Analysis Location', Unicode(255)),
    Column('Analysis Location Description', Unicode(4000)),
    Column('Laboratory Qualifiers', Unicode(255)),
    Column('Laboratory Test Name', Unicode(255)),
    Column('Leachate Preparation Method', Unicode(255)),
    Column('Material Size Removed', DECIMAL(19, 10)),
    Column('Percentage Removed', DECIMAL(19, 10)),
    Column('Remarks', Unicode(4000)),
    Column('Status', Unicode(255)),
    Column('Test Name', Unicode(255)),
    Column('Test Number', Unicode(255)),
    Column('TIC Probability', DECIMAL(19, 10)),
    Column('TIC Retention Time', DECIMAL(19, 10)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3))
)


t_VIEW_Contamination_Summary_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Contamination_Summary_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Determinand', Unicode(255)),
    Column('Determinand Description', Unicode(4000)),
    Column('Unit', Unicode(255)),
    Column('Test Type', Unicode(255)),
    Column('Test Type Description', Unicode(4000)),
    Column('#Min Min', DECIMAL(19, 10)),
    Column('#Max Max', DECIMAL(19, 10)),
    Column('#Sum Number of Readings', Integer)
)


t_VIEW_Contamination_Summary_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Contamination_Summary_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('LocationID', Unicode(255)),
    Column('Geology Code', Unicode(255)),
    Column('Legend Code', Unicode(255)),
    Column('SampleId', Unicode(255)),
    Column('SampleReference', Unicode(255)),
    Column('Sample Type', Unicode(255)),
    Column('DepthTop', DECIMAL(9, 3)),
    Column('DepthBase', DECIMAL(9, 3)),
    Column('Determinand', Unicode(255)),
    Column('Determinand Description', Unicode(4000)),
    Column('Unit', Unicode(255)),
    Column('Test Type', Unicode(255)),
    Column('Test Type Description', Unicode(4000)),
    Column('#Min Minimum', DECIMAL(38, 10)),
    Column('#Max Maximum', DECIMAL(38, 10)),
    Column('#Avg Average', DECIMAL(38, 10)),
    Column('#Sum Count', Integer)
)


t_VIEW_Coring_below_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Coring_below_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('LocationID', Unicode(255)),
    Column('FinalDepth', DECIMAL(9, 3)),
    Column('DepthTop', DECIMAL(9, 3)),
    Column('DepthBase', DECIMAL(9, 3)),
    Column('TCR', DECIMAL(19, 10)),
    Column('SCR', DECIMAL(19, 10)),
    Column('RQD', DECIMAL(19, 10))
)


t_VIEW_Coring_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Coring_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Location ID', Unicode(255)),
    Column('Value', Unicode(255)),
    Column('Expr3', Unicode(4000)),
    Column('DepthBase', DECIMAL(9, 3)),
    Column('DepthTop', DECIMAL(9, 3)),
    Column('Diameter', DECIMAL(19, 10)),
    Column('Duration', BigInteger),
    Column('Remarks', Unicode(4000)),
    Column('RQD', DECIMAL(19, 10)),
    Column('SCR', DECIMAL(19, 10)),
    Column('TCR', DECIMAL(19, 10)),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code 2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Description', Unicode(4000)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Geol Top', DECIMAL(9, 3)),
    Column('Geol Base', DECIMAL(9, 3))
)


t_VIEW_Depth_Information_to_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Depth_Information_to_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Location ID', Unicode(255)),
    Column('Final Depth', DECIMAL(9, 3)),
    Column('Max Base Depth', DECIMAL(9, 3))
)


t_VIEW_Discontinuities_below_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Discontinuities_below_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('LocationID', Unicode(255)),
    Column('FinalDepth', DECIMAL(9, 3)),
    Column('DepthTop', DECIMAL(9, 3)),
    Column('DepthBase', DECIMAL(9, 3)),
    Column('DiscontinuitySetReference', Unicode(255)),
    Column('DiscontinuityReference', Unicode(255)),
    Column('Type', Unicode(255)),
    Column('Dip', DECIMAL(19, 10)),
    Column('DipDirection', DECIMAL(19, 10))
)


t_VIEW_DynamicProbe_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_DynamicProbe_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code 2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geology Description', Unicode(4000)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Test Number', Unicode(255)),
    Column('Probe Type', Unicode(255)),
    Column('Test Date', DATETIME2),
    Column('Anvil Type', Unicode(255)),
    Column('Anvil Damper Type', Unicode(255)),
    Column('Blow Count Frequency', Unicode(255)),
    Column('Cone Angle', DECIMAL(19, 10)),
    Column('Cone Diameter', DECIMAL(19, 10)),
    Column('Final Cone Depth', DECIMAL(9, 3)),
    Column('Ground Water Level', DECIMAL(19, 10)),
    Column('Hammer Mass', DECIMAL(19, 10)),
    Column('Method', Unicode(255)),
    Column('Organisation Name', Unicode(255)),
    Column('PreDrilling', Unicode(255)),
    Column('Rod Diameter', DECIMAL(19, 10)),
    Column('Rod Friction Precautions', Unicode(255)),
    Column('Rod Mass', DECIMAL(19, 10)),
    Column('Standard Drop', DECIMAL(19, 10)),
    Column('Weather', Unicode(255)),
    Column('Depth Top', DECIMAL(9, 3)),
    Column('Blows Increment', DECIMAL(19, 10)),
    Column('Blows Culmative', DECIMAL(19, 10)),
    Column('Delay', BigInteger),
    Column('Depth Increment', DECIMAL(9, 3)),
    Column('Torque', DECIMAL(19, 10))
)


t_VIEW_Gap_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Gap_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('GapTop', DECIMAL(9, 3)),
    Column('GapBase', DECIMAL(9, 3)),
    Column('LocationID', Unicode(255)),
    Column('FinalDepth', DECIMAL(9, 3))
)


t_VIEW_Geology_Summary_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Geology_Summary_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('#Min Min Top Depth', DECIMAL(9, 3)),
    Column('#Max Max Base Depth', DECIMAL(9, 3)),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000))
)


t_VIEW_Geology_to_Final_depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Geology_to_Final_depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Location ID', Unicode(255)),
    Column('Final Depth', DECIMAL(9, 3)),
    Column('Max Base Depth', DECIMAL(9, 3))
)


t_VIEW_Grading_Envelope_by_Geology_Code_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Grading_Envelope_by_Geology_Code_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Particle Size', DECIMAL(19, 10)),
    Column('#Min Min Percentage Passing', DECIMAL(19, 10)),
    Column('#Max Max Percentage Passing', DECIMAL(19, 10))
)


t_VIEW_Grading_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Grading_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geology Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Top Depth', DECIMAL(9, 3)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Reference', Unicode(255)),
    Column('Base Depth', DECIMAL(9, 3)),
    Column('Specimen Depth', DECIMAL(9, 3)),
    Column('Specimen Reference', Unicode(255)),
    Column('Specimen Description', Unicode(4000)),
    Column('Specimen Preparation', Unicode(255)),
    Column('Uniformity Coefficient', DECIMAL(19, 10)),
    Column('Clay Percentage', DECIMAL(19, 10)),
    Column('Silt Percentage', DECIMAL(19, 10)),
    Column('Sand Percentage', DECIMAL(19, 10)),
    Column('Gravel Percentage', DECIMAL(19, 10)),
    Column('Cobbles Percentage', DECIMAL(19, 10)),
    Column('Fines Percentage', DECIMAL(19, 10)),
    Column('Particle Size', DECIMAL(19, 10)),
    Column('Percentage Passing', DECIMAL(19, 10)),
    Column('Test Type', Unicode(255)),
    Column('Test Type Description', Unicode(4000)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3))
)


t_VIEW_Hole_Diameter_to_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Hole_Diameter_to_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Location ID', Unicode(255)),
    Column('Final Depth', DECIMAL(9, 3)),
    Column('Max Base Depth', DECIMAL(9, 3))
)


t_VIEW_Incorrect_Coring_Results_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Incorrect_Coring_Results_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationID', Unicode(255)),
    Column('DepthTop', DECIMAL(9, 3)),
    Column('DepthBase', DECIMAL(9, 3)),
    Column('TCR', DECIMAL(19, 10)),
    Column('SCR', DECIMAL(19, 10)),
    Column('RQD', DECIMAL(19, 10))
)


t_VIEW_Insitu_Testing_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Insitu_Testing_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Location ID', Unicode(255)),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code 2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geology Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3)),
    Column('Geology Thickness', DECIMAL(38, 3)),
    Column('Test Depth', DECIMAL(9, 3)),
    Column('N', DECIMAL(38, 0)),
    Column('Reported Result', Unicode(255)),
    Column('CBR Value', DECIMAL(19, 10)),
    Column('Bulk Density', DECIMAL(19, 10)),
    Column('Hand Pen Value', DECIMAL(19, 10)),
    Column('Permeability Result', DECIMAL(28, 19)),
    Column('Permeability Result Text', Unicode(30)),
    Column('Redox Potential', DECIMAL(19, 10)),
    Column('Resistivity MSP', DECIMAL(19, 10)),
    Column('TestNumber', Unicode(255)),
    Column('InsituVane Result', Unicode(255)),
    Column('InsituVane Residual Result', Unicode(255)),
    Column('FID Result', DECIMAL(19, 10)),
    Column('PID Result', DECIMAL(19, 10)),
    Column('Soakaway Fill Porosity', DECIMAL(19, 10)),
    Column('Soakaway Infiltration Rate', DECIMAL(28, 19))
)


t_VIEW_Laboratory_CBR_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Laboratory_CBR_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Top Depth', DECIMAL(9, 3)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Reference', Unicode(255)),
    Column('Base Depth', DECIMAL(9, 3)),
    Column('Specimen Depth', DECIMAL(9, 3)),
    Column('Specimen Reference', Unicode(255)),
    Column('Specimen Description', Unicode(4000)),
    Column('Specimen Preparation', Unicode(255)),
    Column('Sample Condition', Unicode(255)),
    Column('Natural Moisture Content', DECIMAL(19, 10)),
    Column('Percentage Passing', DECIMAL(19, 10)),
    Column('Sieve Size', DECIMAL(19, 10)),
    Column('Total Swell', DECIMAL(19, 10)),
    Column('Test No', Unicode(255)),
    Column('Initial Bulk Density', DECIMAL(19, 10)),
    Column('Initial Dry Density', DECIMAL(19, 10)),
    Column('Initial Moisture Content', DECIMAL(19, 10)),
    Column('CBR Top', DECIMAL(19, 10)),
    Column('CBR Base', DECIMAL(19, 10)),
    Column('Moisture Content Top', DECIMAL(19, 10)),
    Column('Moisture Content Base', DECIMAL(19, 10)),
    Column('Soaking Details', Unicode(4000)),
    Column('Soaking Swelling', DECIMAL(19, 10)),
    Column('Surcharge Pressure', DECIMAL(19, 10)),
    Column('Test Remarks', Unicode(4000)),
    Column('General Remarks', Unicode(4000)),
    Column('Method', Unicode(255)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3))
)


class VIEWLinkedDocumentsMetadatum(Base):
    __tablename__ = 'VIEW_LinkedDocumentsMetadata'

    Id = Column(UNIQUEIDENTIFIER, primary_key=True)
    sysUser = Column(UNIQUEIDENTIFIER)
    sysDate = Column(DateTime, index=True)
    sysAction = Column(Unicode(255), index=True)
    sysActionDesc = Column(Unicode(255))
    Snapshot = Column(UNIQUEIDENTIFIER, index=True)
    Project = Column(UNIQUEIDENTIFIER, index=True)


t_VIEW_Location_Geology_Summary_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Location_Geology_Summary_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationID', Unicode(255)),
    Column('Top Depth', DECIMAL(9, 3)),
    Column('Base Depth', DECIMAL(9, 3)),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000))
)


t_VIEW_Location_Monitoring_Summary_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Location_Monitoring_Summary_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Location ID', Unicode(255)),
    Column('Type', Unicode(255)),
    Column('Type Description', Unicode(4000)),
    Column('First Reading', DATETIME2),
    Column('Last Reading', DATETIME2),
    Column('Number of Readings', Integer),
    Column('Min Reading', DECIMAL(19, 10)),
    Column('Max Reading', DECIMAL(19, 10))
)


t_VIEW_MCV_By_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_MCV_By_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationID', Unicode(255)),
    Column('GeologyCode', Unicode(255)),
    Column('GeologyCodeDescription', Unicode(4000)),
    Column('GeologyDescription', Unicode(4000)),
    Column('GeologyCode2', Unicode(255)),
    Column('GeologyCode2Description', Unicode(4000)),
    Column('LegendCode', Unicode(255)),
    Column('LegendCodeDescription', Unicode(4000)),
    Column('GeologyFormation', Unicode(255)),
    Column('BGSLexicon', Unicode(255)),
    Column('BGSLexiconDescription', Unicode(4000)),
    Column('SampleTop', DECIMAL(9, 3)),
    Column('SampleReference', Unicode(255)),
    Column('SampleType', Unicode(255)),
    Column('SampleID', Unicode(255)),
    Column('SampleBase', DECIMAL(9, 3)),
    Column('SpecimenTop', DECIMAL(9, 3)),
    Column('SpecimenReference', Unicode(255)),
    Column('SpecimenDescription', Unicode(4000)),
    Column('SpecimenPreparation', Unicode(255)),
    Column('NMC', DECIMAL(19, 10)),
    Column('PercentagePassing', DECIMAL(19, 10)),
    Column('SieveSize', DECIMAL(19, 10)),
    Column('PrecalibratedValue', Unicode(255)),
    Column('StabiliserAmount', DECIMAL(19, 10)),
    Column('StabiliserType', Unicode(255)),
    Column('TestNumber', Unicode(255)),
    Column('MCV', DECIMAL(19, 10)),
    Column('MoistureContent', DECIMAL(19, 10)),
    Column('BulkDensity', DECIMAL(19, 10)),
    Column('BlowDifference', DECIMAL(19, 10)),
    Column('StrengthAgainstStandard', Unicode(255))
)


t_VIEW_MONR_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_MONR_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('GeologyCode', Unicode(255)),
    Column('GeologyCodeDescription', Unicode(4000)),
    Column('GeologyDescription', Unicode(4000)),
    Column('GeologyCode2', Unicode(255)),
    Column('GeologyCode2Description', Unicode(4000)),
    Column('LegendCode', Unicode(255)),
    Column('LegendCodeDescription', Unicode(4000)),
    Column('GeologyFormation', Unicode(255)),
    Column('BGSLexicon', Unicode(255)),
    Column('BGSLexiconDescription', Unicode(4000)),
    Column('LocationID', Unicode(255)),
    Column('PointReference', Unicode(255)),
    Column('InstrumentType', Unicode(255)),
    Column('Distance', DECIMAL(19, 10)),
    Column('BearingA', DECIMAL(19, 10)),
    Column('BearingB', DECIMAL(19, 10)),
    Column('BearingC', DECIMAL(19, 10)),
    Column('DateInstallation', DATETIME2),
    Column('ResponseZoneTop', DECIMAL(9, 3)),
    Column('ResponseZoneBase', DECIMAL(9, 3)),
    Column('InclinationA', DECIMAL(19, 10)),
    Column('InclinationB', DECIMAL(19, 10)),
    Column('InclinationC', DECIMAL(19, 10)),
    Column('InstallationDetails', Unicode(4000)),
    Column('PipeReference', Unicode(255)),
    Column('SignConventionA', Unicode(255)),
    Column('SignConventionB', Unicode(255)),
    Column('SignConventionC', Unicode(255)),
    Column('DateTime', DATETIME2),
    Column('Reading', DECIMAL(19, 10)),
    Column('Unit', Unicode(255)),
    Column('InstrumentDetectionLimit', DECIMAL(19, 10)),
    Column('Reference', Unicode(255)),
    Column('InstrumentUpperLimit', DECIMAL(19, 10)),
    Column('MeasurementName', Unicode(255)),
    Column('ReadingReference', Unicode(255)),
    Column('ReadingText', Unicode(255)),
    Column('ReadingType', Unicode(255)),
    Column('TestType', Unicode(255))
)


t_VIEW_Missing_Geology_Codes_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Missing_Geology_Codes_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Location ID', Unicode(255)),
    Column('Empty Geology Codes', Integer)
)


t_VIEW_Missing_Legend_Codes_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Missing_Legend_Codes_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Location ID', Unicode(255)),
    Column('Empty Legend Codes', Integer)
)


t_VIEW_Overlapping_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Overlapping_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationID', Unicode(255)),
    Column('DepthTop', DECIMAL(9, 3)),
    Column('DepthBase', DECIMAL(9, 3)),
    Column('OverlappingTopDepth', DECIMAL(9, 3)),
    Column('OverlappingBaseDepth', DECIMAL(9, 3))
)


t_VIEW_Perm_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Perm_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code 2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geology Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3)),
    Column('Location ID', Unicode(255)),
    Column('Depth Top', DECIMAL(9, 3)),
    Column('Depth Base', DECIMAL(9, 3)),
    Column('Test Number', Unicode(255)),
    Column('Test Type', Unicode(255)),
    Column('Permeability Result', DECIMAL(28, 19)),
    Column('Permeability Result Text', Unicode(30)),
    Column('Depth Standing Water', DECIMAL(9, 3)),
    Column('Water Depth Before Test', Unicode(50)),
    Column('Water Depth at Start of Test', Unicode(50)),
    Column('Casing Diameter', DECIMAL(19, 10)),
    Column('Test Zone Diameter', DECIMAL(19, 10)),
    Column('Method', Unicode(255)),
    Column('Applied Head of Water', DECIMAL(19, 10)),
    Column('Average Flow', DECIMAL(19, 10)),
    Column('Organisation Name', Unicode(255)),
    Column('Stage Number', DECIMAL(19, 10)),
    Column('Weather', Unicode(255)),
    Column('Status', Unicode(255)),
    Column('Water Depth', Unicode(50)),
    Column('Time Elapsed', BigInteger)
)


t_VIEW_SPT_below_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_SPT_below_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('LocationID', Unicode(255)),
    Column('FinalDepth', DECIMAL(9, 3)),
    Column('DepthTop', DECIMAL(9, 3)),
    Column('NValue', DECIMAL(19, 10)),
    Column('ReportedResult', Unicode(255))
)


t_VIEW_SPT_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_SPT_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code 2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geology Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('SPT Top Depth', DECIMAL(9, 3)),
    Column('N', DECIMAL(19, 10)),
    Column('Reported Result', Unicode(255)),
    Column('Energy Ratio', DECIMAL(19, 10)),
    Column('Main Blows', DECIMAL(19, 10)),
    Column('Seating Blows', DECIMAL(19, 10)),
    Column('Total Penetration', DECIMAL(19, 10)),
    Column('Seating Penetration 1', DECIMAL(19, 10)),
    Column('Seating Blows 1', DECIMAL(19, 10)),
    Column('Seating Penetration 2', DECIMAL(19, 10)),
    Column('Seating Blows 2', DECIMAL(19, 10)),
    Column('Main Penetration 1', DECIMAL(19, 10)),
    Column('Main Blows 1', DECIMAL(19, 10)),
    Column('Main Penetration 2', DECIMAL(19, 10)),
    Column('Main Blows 2', DECIMAL(19, 10)),
    Column('Main Penetration 3', DECIMAL(19, 10)),
    Column('Main Blows 3', DECIMAL(19, 10)),
    Column('Main Penetration 4', DECIMAL(19, 10)),
    Column('Main Blows 4', DECIMAL(19, 10)),
    Column('Casing Depth', DECIMAL(9, 3)),
    Column('Water Depth', Unicode(255)),
    Column('Self Weight Penetration', DECIMAL(19, 10)),
    Column('Test Type', Unicode(255)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3))
)


t_VIEW_Sample_Counts_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Sample_Counts_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Sample Type', Unicode(255)),
    Column('Sample Type Description', Unicode(4000)),
    Column('#Sum Count', Integer)
)


t_VIEW_Sample_Counts_by_Location_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Sample_Counts_by_Location_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Location ID', Unicode(255)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Type Description', Unicode(4000)),
    Column('#Sum Count', Integer)
)


t_VIEW_Samples_below_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Samples_below_Final_Depth_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('LocationID', Unicode(255)),
    Column('FinalDepth', DECIMAL(9, 3)),
    Column('SampleReference', Unicode(255)),
    Column('Sample Type', Unicode(255)),
    Column('DepthTop', DECIMAL(9, 3)),
    Column('DepthBase', DECIMAL(9, 3)),
    Column('SampleID', Unicode(255))
)


t_VIEW_Samples_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Samples_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code 2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code Steve', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geology Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Top Depth', DECIMAL(9, 3)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Reference', Unicode(255)),
    Column('Base Depth', DECIMAL(9, 3)),
    Column('Containner', Unicode(255)),
    Column('Sample ID', Unicode(255)),
    Column('Matrix', Unicode(255)),
    Column('Method', Unicode(255)),
    Column('QA Type', Unicode(255)),
    Column('Preparation', Unicode(255)),
    Column('Diameter', DECIMAL(19, 10)),
    Column('Sample Description', Unicode(4000)),
    Column('Classification', Unicode(255)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3))
)


t_VIEW_Shear_Box_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Shear_Box_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Top Depth', DECIMAL(9, 3)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Reference', Unicode(255)),
    Column('Base Depth', DECIMAL(9, 3)),
    Column('Specimen Depth', DECIMAL(9, 3)),
    Column('Specimen Reference', Unicode(255)),
    Column('Specimen Description', Unicode(4000)),
    Column('Specimen Preparation', Unicode(255)),
    Column('Specimen Condition', Unicode(255)),
    Column('Peak Angle of Friction', DECIMAL(19, 10)),
    Column('Residual Angle of Friction', DECIMAL(19, 10)),
    Column('Peak Cohesion Intercept', DECIMAL(19, 10)),
    Column('Residual Cohesion Intercept', DECIMAL(19, 10)),
    Column('Specimen Condition Statement', Unicode(255)),
    Column('Test Type', Unicode(255)),
    Column('Remarks', Unicode(4000)),
    Column('Method', Unicode(255)),
    Column('Encapsulation Method', Unicode(255)),
    Column('Status', Unicode(255)),
    Column('Criterion', Unicode(255)),
    Column('Diameter', DECIMAL(19, 10)),
    Column('Perpendicular Diameter', DECIMAL(19, 10)),
    Column('Initial Bulk Density', DECIMAL(19, 10)),
    Column('Initial Dry Density', DECIMAL(19, 10)),
    Column('Initial Voids Ratio', DECIMAL(19, 10)),
    Column('Initial Moisture Content', DECIMAL(19, 10)),
    Column('Final Moisture Content', DECIMAL(19, 10)),
    Column('Number of Traverses', DECIMAL(19, 10)),
    Column('Normal Stress', DECIMAL(19, 10)),
    Column('Particle Density', DECIMAL(19, 10)),
    Column('Particle Density Method', Unicode(255)),
    Column('Test No', Unicode(255)),
    Column('Specimen Height', DECIMAL(19, 10)),
    Column('Peak Shear Stress', DECIMAL(19, 10)),
    Column('Peak Stress Displacement \nRate', DECIMAL(19, 10)),
    Column('Peak Stress Horizontal Displacement', DECIMAL(19, 10)),
    Column('Peak Stress Vertical Displacement', DECIMAL(19, 10)),
    Column('Test Remarks', Unicode(4000)),
    Column('Residual Shear Stress', DECIMAL(19, 10)),
    Column('Residual Stress Displacement Rate', DECIMAL(19, 10)),
    Column('Residual Stress Horizontal Displacement', DECIMAL(19, 10)),
    Column('Residual Stress Vertical Displacement', DECIMAL(19, 10)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3))
)


t_VIEW_Triaxial_Effective_Stress_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Triaxial_Effective_Stress_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Top Depth', DECIMAL(9, 3)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Reference', Unicode(255)),
    Column('Base Depth', DECIMAL(9, 3)),
    Column('Specimen Depth', DECIMAL(9, 3)),
    Column('Specimen Reference', Unicode(255)),
    Column('Specimen Description', Unicode(4000)),
    Column('Specimen Preparation', Unicode(255)),
    Column('Specimen Condition', Unicode(255)),
    Column('Specimen Condition Description', Unicode(4000)),
    Column('Test Type', Unicode(255)),
    Column('Test Type Description', Unicode(4000)),
    Column('Cohesion Intercept', DECIMAL(19, 10)),
    Column('Cu', DECIMAL(19, 10)),
    Column('Phi', DECIMAL(19, 10)),
    Column('Initial Bulk Density', DECIMAL(19, 10)),
    Column('Initial Dry Density', DECIMAL(19, 10)),
    Column('Initial Moisture Content', DECIMAL(19, 10)),
    Column('Remarks', Unicode(4000)),
    Column('Status', Unicode(255)),
    Column('Method', Unicode(255)),
    Column('Failure Criterion', Unicode(255)),
    Column('Diameter', DECIMAL(19, 10)),
    Column('Specimen Length', DECIMAL(19, 10)),
    Column('Initial Pore Pressure', DECIMAL(19, 10)),
    Column('Cell Pressure', DECIMAL(19, 10)),
    Column('Axail Strain Rate', DECIMAL(19, 10)),
    Column('Axial Strain at Failure', DECIMAL(19, 10)),
    Column('Deviator Stress at Failure', DECIMAL(19, 10)),
    Column('Pore Pressure at Failure', DECIMAL(19, 10)),
    Column('Volumetric Strain at Failure', DECIMAL(19, 10)),
    Column('Failure Mode', Unicode(255)),
    Column('Final Moisture Content', DECIMAL(19, 10)),
    Column('Stage Remarks', Unicode(4000)),
    Column('Test Number', Unicode(255)),
    Column('Saturation Details', Unicode(255)),
    Column('Consolidation Details', Unicode(255)),
    Column('EffectiveStressEnd', DECIMAL(19, 10)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3))
)


t_VIEW_Triaxial_Total_Stress_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Triaxial_Total_Stress_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER),
    Column('Geology Code', Unicode(255)),
    Column('Geology Code Description', Unicode(4000)),
    Column('Geology Code2', Unicode(255)),
    Column('Geology Code 2 Description', Unicode(4000)),
    Column('Legend Code', Unicode(255)),
    Column('Legend Code Description', Unicode(4000)),
    Column('Geological Formation', Unicode(255)),
    Column('BGS Lexicon', Unicode(255)),
    Column('BGS Lexicon Description', Unicode(4000)),
    Column('Location ID', Unicode(255)),
    Column('Top Depth', DECIMAL(9, 3)),
    Column('Sample Type', Unicode(255)),
    Column('Sample Reference', Unicode(255)),
    Column('Base Depth', DECIMAL(9, 3)),
    Column('Specimen Depth', DECIMAL(9, 3)),
    Column('Specimen Reference', Unicode(255)),
    Column('Specimen Description', Unicode(4000)),
    Column('Specimen Preparation', Unicode(255)),
    Column('Specimen Condition', Unicode(255)),
    Column('Specimen Condition Description', Unicode(4000)),
    Column('Test Type', Unicode(255)),
    Column('Test Type Description', Unicode(4000)),
    Column('Cohesion Intercept', DECIMAL(19, 10)),
    Column('Cu', DECIMAL(19, 10)),
    Column('Phi', DECIMAL(19, 10)),
    Column('Initial Bulk Density', DECIMAL(19, 10)),
    Column('Initial Dry Density', DECIMAL(19, 10)),
    Column('Initial Moisture Content', DECIMAL(19, 10)),
    Column('Remarks', Unicode(4000)),
    Column('Status', Unicode(255)),
    Column('Method', Unicode(255)),
    Column('Diameter', DECIMAL(19, 10)),
    Column('Specimen Length', DECIMAL(19, 10)),
    Column('Cell Pressure', DECIMAL(19, 10)),
    Column('Axial Strain at Failure', DECIMAL(19, 10)),
    Column('Corrected Deviator Stress at Failure', DECIMAL(19, 10)),
    Column('Failure Mode', Unicode(255)),
    Column('Shear Strength at Failure', DECIMAL(19, 10)),
    Column('Final Moisture Content', DECIMAL(19, 10)),
    Column('Stage Remarks', Unicode(4000)),
    Column('Test Number', Unicode(255)),
    Column('Geology Top Depth', DECIMAL(9, 3)),
    Column('Geology Base Depth', DECIMAL(9, 3))
)


t_VIEW_UniqueSamples_Summary_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_UniqueSamples_Summary_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationID', Unicode(255)),
    Column('DepthTop', DECIMAL(9, 3)),
    Column('Value', Unicode(255)),
    Column('SampleReference', Unicode(255)),
    Column('DepthBase', DECIMAL(9, 3)),
    Column('ScheduleReference', Unicode(255)),
    Column('SampleID', Unicode(255))
)


t_VIEW_ViewProjectUser = Table(
    'VIEW_ViewProjectUser', metadata,
    Column('Id', UNIQUEIDENTIFIER, nullable=False),
    Column('user', UNIQUEIDENTIFIER, nullable=False),
    Column('Current', BIT, nullable=False),
    Column('sysAction', Unicode(255)),
    Column('Project', UNIQUEIDENTIFIER, nullable=False)
)


t_VIEW_Water_Strike_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073 = Table(
    'VIEW_Water_Strike_by_Geology_75e8ce5a_7ae0_41ca_86f0_aca1e7158073', metadata,
    Column('LocationDetails', UNIQUEIDENTIFIER, nullable=False),
    Column('LocationID', Unicode(255)),
    Column('GeologyCode', Unicode(255)),
    Column('GeologyCodeDescription', Unicode(4000)),
    Column('GeologyDescription', Unicode(4000)),
    Column('GeologyCode2', Unicode(255)),
    Column('GeologyCode2Description', Unicode(4000)),
    Column('LegendCode', Unicode(255)),
    Column('LegendCodeDescription', Unicode(4000)),
    Column('GeologyFormation', Unicode(255)),
    Column('BGSLexicon', Unicode(255)),
    Column('BGSLexiconDescription', Unicode(4000)),
    Column('Ground Water Strike', DECIMAL(9, 3)),
    Column('StrikeTime', DATETIME2),
    Column('CasingDepth', DECIMAL(9, 3)),
    Column('SealedDepth', DECIMAL(9, 3)),
    Column('GeneralRemarks', Unicode(4000)),
    Column('Water Level', DECIMAL(12, 3)),
    Column('TimeElapsed', DECIMAL(19, 10)),
    Column('DetailRemarks', Unicode(4000))
)
