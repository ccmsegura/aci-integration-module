# Copyright (c) 2018 Cisco Systems
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Support utf-8 constrained indexed columns

Revision ID: 33182aa94990
Revises: f1ca776aafab
Create Date: 2018-03-12 12:23:39.608507

"""

# revision identifiers, used by Alembic.
revision = '33182aa94990'
down_revision = '2b48bf7f19cb'
branch_labels = None
depends_on = None

from aim.api import types as t
from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('aim_security_group_rules',
                  sa.Column('icmp_type', sa.String(16),
                            server_default=t.UNSPECIFIED, nullable=False))
    op.add_column('aim_security_group_rules',
                  sa.Column('icmp_code', sa.String(16),
                            server_default=t.UNSPECIFIED, nullable=False))


def downgrade():
    pass
