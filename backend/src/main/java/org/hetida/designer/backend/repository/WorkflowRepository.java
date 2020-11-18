package org.hetida.designer.backend.repository;

import org.hetida.designer.backend.model.Workflow;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.UUID;

public interface WorkflowRepository extends JpaRepository<Workflow, UUID> {
    List<Workflow> findAllById(Iterable<UUID> ids);
}
