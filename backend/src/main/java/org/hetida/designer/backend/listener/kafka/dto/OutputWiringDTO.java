package org.hetida.designer.backend.listener.kafka.dto;

import lombok.Data;

@Data
public class OutputWiringDTO {
    private String workflow_output_name;
    private Integer adapter_id;
    private String sink_id;
}
