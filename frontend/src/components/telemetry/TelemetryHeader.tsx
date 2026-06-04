"use client";

import React from 'react';
import { useTelemetryContext } from '@/lib/telemetry-context';

export const TelemetryHeader: React.FC = () => {
  const { drivers, selectedDriverId } = useTelemetryContext();

  // Fix for the no-undef 'currentDriver' issue
  const currentDriver = drivers.find(d => d.id === selectedDriverId);

  // Safeguard against undefined lapData and currentDriver
  const currentLap = currentDriver?.lapData?.[currentDriver.lapData.length - 1];

  return (
    <div className="w-full bg-zinc-900 text-white p-4 rounded-xl border border-zinc-800 shadow-lg mb-6">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-xs font-bold text-zinc-500 uppercase tracking-widest mb-1">Live Telemetry</h3>
          <div className="flex items-center gap-3">
            <span className="text-xl font-bold">{currentDriver?.name || 'No Driver Selected'}</span>
            {currentDriver && (
              <span className="px-2 py-0.5 bg-green-500/20 text-green-500 text-[10px] font-bold rounded border border-green-500/30">
                ACTIVE
              </span>
            )}
          </div>
        </div>

        {currentLap && (
          <div className="text-right">
            <div className="text-[10px] text-zinc-500 font-bold uppercase mb-1">Last Lap</div>
            <div className="text-2xl font-mono font-bold text-green-400 leading-none">
              {currentLap.time}
            </div>
            <div className="text-[10px] text-zinc-600 mt-1">Lap {currentLap.lap}</div>
          </div>
        )}
      </div>

      {drivers.length > 0 && (
        <div className="mt-4 flex gap-2 overflow-x-auto pb-2">
          {drivers.map(driver => (
            <div
              key={driver.id}
              className={`flex-shrink-0 px-3 py-1.5 rounded-lg text-xs font-medium border transition-colors ${
                driver.id === selectedDriverId
                  ? 'bg-zinc-800 border-zinc-600 text-white'
                  : 'bg-zinc-950 border-zinc-800 text-zinc-500'
              }`}
            >
              {driver.name}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
