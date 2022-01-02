
low_level_metrics = {
    # dora kpis:
    "projector_deployment[deployment_status]":["Change failure rate",
                                               "Deployment frequency",
                                               ],
    "v_projector_deployment_change_leadtime[median_time_to_change]":["Lead time for changes",],
    "projector_incidents[resolvedtime]":["Time to restore services",],
    # fp metrics:
    "projector_workitem[timestamp_done]":["Average throughput rate",
                                          "Average user story lead time",
                                          "Average user story cycle time",
                                          "Average user story wait time",
                                          "Average lead time to defect",
                                          "Average cycle time to defect",
                                          "Average wait time to defect",],
    "projector_teamsize[team_size]":["Average throughput rate"],
    "projector_workitem[date_in_progress]":["Work in Progress",],
    "projector_workitem[date_ready]":["Work in Progress",],
    "meta_workitemtypemapping[final_type_name]":["Average user story lead time",
                                                 "Average user story cycle time",
                                                 "Average user story wait time",
                                                 "Average lead time to defect",
                                                 "Average cycle time to defect",
                                                 "Average wait time to defect",],
    "projector_repository[Repo Activity]":["Average repository activity",
                                           ],
    "projector_pullrequestsize[Total lines]":["Average Pull Request Size",
                                              ],
    "projector_pipelinerun[Fix Time]":["Build frequency",
                                       "Average time to fix broken build",
                                       ],
    "projector_pipelinerun[Run Time]":["Average build execution time",
                                       ],
    "projector_measure[Rating High]":["Build health factors",
                                      ],
    "projector_measure[Coverage]":["Unit test coverage",
                                   ],
    "projector_pullrequestsize[date_diff]":["Average pull request lead time"],
}