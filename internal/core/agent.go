package core

import (
	"fmt"
)

type AgentAdapter interface {
	Processes() []*Process
	Start() error
	Stop() error
	Install() error
	Update() error
	Config() error
}

type Agent struct {
	Adapter AgentAdapter
}

func NewAgent(a AgentAdapter) *Agent {
	return &Agent{Adapter: a}
}

func (a *Agent) Active() bool {
	if len(a.Adapter.Processes()) == 0 {
		return false
	}

	for _, p := range a.Adapter.Processes() {
		if !p.Active() {
			return false
		}
	}
	return true
}

func (a *Agent) Start() error {
	if a.Active() {
		return fmt.Errorf("agent active, no need start")
	}

	if err := a.Adapter.Config(); err != nil {
		return err
	}
	return a.Adapter.Start()
}

func (a *Agent) Stop() error {
	if !a.Active() {
		return fmt.Errorf("agent inactive, no need stop")
	}

	return a.Adapter.Stop()
}

func (a *Agent) Restart() error {
	if a.Active() {
		if err := a.Stop(); err != nil {
			return err
		}
	}
	return a.Start()
}

func (a *Agent) Update() error {
	active := a.Active()

	if active {
		if err := a.Stop(); err != nil {
			return err
		}
	}
	if err := a.Adapter.Update(); err != nil {
		return err
	}

	if active {
		if err := a.Start(); err != nil {
			return err
		}
	}
	return nil
}

func (a *Agent) Install() error {
	if a.Active() {
		if err := a.Stop(); err != nil {
			return err
		}
	}
	return a.Adapter.Install()
}