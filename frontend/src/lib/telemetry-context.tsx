"use client";

import React, { createContext, useContext, useState } from 'react';

export interface LapData {
  lap: number;
  time: string;
}

export interface Driver {
  id: string;
  name: string;
  lapData: LapData[];
}

interface TelemetryContextType {
  drivers: Driver[];
  selectedDriverId: string | null;
  setSelectedDriverId: (id: string | null) => void;
}

const TelemetryContext = createContext<TelemetryContextType | undefined>(undefined);

const INITIAL_DRIVERS: Driver[] = [
  {
    id: '1',
    name: 'Autonomous Agent Alpha',
    lapData: [
      { lap: 1, time: '1:24.5' },
      { lap: 2, time: '1:23.8' }
    ]
  },
  {
    id: '2',
    name: 'System Bot Beta',
    lapData: [
      { lap: 1, time: '1:25.1' },
      { lap: 2, time: '1:24.2' }
    ]
  }
];

export function TelemetryProvider({ children }: { children: React.ReactNode }) {
  const [drivers] = useState<Driver[]>(INITIAL_DRIVERS);
  const [selectedDriverId, setSelectedDriverId] = useState<string | null>(
    INITIAL_DRIVERS.length > 0 ? INITIAL_DRIVERS[0].id : null
  );

  return (
    <TelemetryContext.Provider value={{ drivers, selectedDriverId, setSelectedDriverId }}>
      {children}
    </TelemetryContext.Provider>
  );
}

export function useTelemetryContext() {
  const context = useContext(TelemetryContext);
  if (context === undefined) {
    throw new Error('useTelemetryContext must be used within a TelemetryProvider');
  }
  return context;
}
