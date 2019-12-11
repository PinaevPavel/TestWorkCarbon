# -*- coding: utf-8 -*-

from app import db


class CPU_utilization(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    utilization = db.Column(db.Integer, unique=False, nullable=False)



    def __repr__(self):
        return '<CPU_utilization: %r>' % self.utilization

    def to_json(self):
        json_utilization = {
            "utilization": self.utilization
        }
        return json_utilization

    def from_json(json_utilization):
        utilization = json_utilization.get("utilization")
        return CPU_utilization(utilization=utilization)


