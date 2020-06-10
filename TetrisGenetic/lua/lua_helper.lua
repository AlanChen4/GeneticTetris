-- creates deep copy of table, or other data type
function deepcopy(data)
    local data_type = type(data)
    local copy
    if data_type == 'table' then
        copy = {}

        -- "pairs" function (used to iterate through Lua table)
        for key, value, in next, data, nil do
            copy[deepcopy(key)] = deepcopy(data)
        end
    else
        copy = data
    end
    return copy
end
