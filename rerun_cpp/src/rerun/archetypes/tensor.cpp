// NOTE: This file was autogenerated by re_types_builder; DO NOT EDIT.
// Based on "crates/re_types/definitions/rerun/archetypes/tensor.fbs"

#include "tensor.hpp"

#include "../components/tensor_data.hpp"

namespace rerun {
    namespace archetypes {
        Result<std::vector<rerun::DataCell>> Tensor::to_data_cells() const {
            std::vector<rerun::DataCell> cells;
            cells.reserve(1);

            {
                const auto result = rerun::components::TensorData::to_data_cell(&data, 1);
                if (result.is_err()) {
                    return result.error;
                }
                cells.emplace_back(std::move(result.value));
            }
            {
                const auto result =
                    create_indicator_component("rerun.components.TensorIndicator", num_instances());
                if (result.is_err()) {
                    return result.error;
                }
                cells.emplace_back(std::move(result.value));
            }

            return cells;
        }
    } // namespace archetypes
} // namespace rerun
