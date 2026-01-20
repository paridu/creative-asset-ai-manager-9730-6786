/**
 * @file StrategyController.js
 * @description Logic for managing the transition from Chaos to Order.
 */

class StrategyController {
  constructor() {
    this.phases = ['INDEXING', 'CLASSIFYING', 'OPTIMIZING', 'CREATING'];
    this.currentStatus = 'CHAOS';
  }

  /**
   * Defines the core logic for the MVP asset discovery.
   */
  calculateValueProposition(timeSpentSearching) {
    const hourlyRate = 50; // Average freelancer rate
    const savedHoursPerMonth = timeSpentSearching * 0.8; 
    const monthlyROI = savedHoursPerMonth * hourlyRate;

    return {
      monthlySavings: `$${monthlyROI}`,
      creativeTimeGain: `${savedHoursPerMonth} hours`
    };
  }

  getRoadmapMilestones() {
    return [
      { id: 1, name: "Project Ghost: Background Indexing", status: "In-Progress" },
      { id: 2, name: "Project Vision: AI Tagging", status: "Planned" },
      { id: 3, name: "Project Bridge: Creative Suite Sync", status: "Backlog" }
    ];
  }
}

export default new StrategyController();