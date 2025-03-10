"""
Copyright 2019 Goldman Sachs.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Tuple

from dataclasses_json import LetterCase, config, dataclass_json

from gs_quant.common import *


class OverlayType(EnumBase, Enum):    
    
    """Type"""

    Payout = 'Payout'
    Price = 'Price'
    MtM = 'MtM'
    Delta = 'Delta'
    Vega = 'Vega'
    Theta = 'Theta'
    RelativeCheapness = 'RelativeCheapness'
    ProbabilityDistribution = 'ProbabilityDistribution'
    _None = 'None'    


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class ChartingParameters(Base):
    spot_style: Optional[str] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class MarketDataParameters(Base):
    max_history: Optional[datetime.date] = field(default=None, metadata=field_metadata)
    timestamp: Optional[datetime.datetime] = field(default=None, metadata=field_metadata)
    spot_ref: Optional[float] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class SolvingTarget(Base):
    constraint: Optional[float] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class OverlayParameters(Base):
    overlay_type: Optional[OverlayType] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class SolvingInfo(Base):
    target: Optional[SolvingTarget] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class VisualStructuringReport(QuoteReport):
    report_type: Optional[str] = field(default='VisualStructuringReport', metadata=field_metadata)
    position_set_id: Optional[str] = field(default=None, metadata=field_metadata)
    quick_entry_text: Optional[str] = field(default=None, metadata=field_metadata)
    as_of_date: Optional[datetime.date] = field(default=None, metadata=field_metadata)
    market_data_parameters: Optional[MarketDataParameters] = field(default=None, metadata=field_metadata)
    overlay_parameters: Optional[OverlayParameters] = field(default=None, metadata=field_metadata)
    solving_info: Optional[SolvingInfo] = field(default=None, metadata=field_metadata)
    charting_parameters: Optional[ChartingParameters] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class SaveQuoteRequest(Base):
    positions: Tuple[PositionSet, ...] = field(default=None, metadata=field_metadata)
    measures: Tuple[RiskMeasure, ...] = field(default=None, metadata=field_metadata)
    pricing_and_market_data_as_of: Optional[Tuple[PricingDateAndMarketDataAsOf, ...]] = field(default=None, metadata=field_metadata)
    pricing_location: Optional[PricingLocation] = field(default=None, metadata=field_metadata)
    scenario: Optional[MarketDataScenario] = field(default=None, metadata=field_metadata)
    parameters: Optional[RiskRequestParameters] = field(default=None, metadata=field_metadata)
    reports: Optional[Tuple[QuoteReport, ...]] = field(default=None, metadata=field_metadata)
    shared_users: Optional[Tuple[str, ...]] = field(default=None, metadata=field_metadata)
    comments: Optional[str] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class WorkflowPosition(Base):
    id_: str = field(default=None, metadata=config(field_name='id', exclude=exclude_none))
    position_sets: Optional[Tuple[PositionSet, ...]] = field(default=None, metadata=field_metadata)
    reports: Optional[Tuple[QuoteReport, ...]] = field(default=None, metadata=field_metadata)
    comments: Optional[str] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class WorkflowPositionsResponse(Base):
    results: Optional[Tuple[WorkflowPosition, ...]] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)
